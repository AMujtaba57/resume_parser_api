import copy
import json
import re
from collections import Counter
import nltk
import numpy as np
from nltk import word_tokenize

from api.models import Keyword, KeywordAlternative, KeywordHistory, Configuration
from api.models import ResultHistory
from parser.industry import industry_classifer
from parser.resume_Industry_classifier import query_classifier_industry
from parser.resume_query_classifier import query_industry_classifier
from similarity.certification import certification_similarity
from similarity.education import education_similarity, query_classify
from similarity.job_title import job_title_similarity
from similarity.js_similarity import exp_query_similarity
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))
tagger = None

CERTIFICATION_WEIGHTAGE = None
EXPERIENCE_WEIGHTAGE = None
TOTAL_QUERIES_WEIGHTAGE = None
EDUCATION_WEIGHTAGE = None
ALTER_KEYWORD_CONFIG = None


def configuration_weightage():
    global CERTIFICATION_WEIGHTAGE, EXPERIENCE_WEIGHTAGE, TOTAL_QUERIES_WEIGHTAGE, EDUCATION_WEIGHTAGE, ALTER_KEYWORD_CONFIG
    EXPERIENCE_WEIGHTAGE = json.dumps(
        Configuration.objects.filter(name='experience_weightage').first().configuration_setting)
    EXPERIENCE_WEIGHTAGE = json.loads(EXPERIENCE_WEIGHTAGE)

    CERTIFICATION_WEIGHTAGE = json.dumps(
        Configuration.objects.filter(name='certification').first().configuration_setting)
    CERTIFICATION_WEIGHTAGE = json.loads(CERTIFICATION_WEIGHTAGE)

    TOTAL_QUERIES_WEIGHTAGE = EXPERIENCE_WEIGHTAGE.get('total_experience', 20)

    EDUCATION_WEIGHTAGE = json.dumps(
        Configuration.objects.filter(name='degree_down_percentage').first().configuration_setting)
    EDUCATION_WEIGHTAGE = json.loads(EDUCATION_WEIGHTAGE)

    ALTER_KEYWORD_CONFIG = json.dumps(
        Configuration.objects.filter(name='alter_keyword_config').first().configuration_setting)
    ALTER_KEYWORD_CONFIG = json.loads(ALTER_KEYWORD_CONFIG)


def load_dataset():
    keywords = Keyword.objects.all()
    model = {str(keyword.keyword_value): str(keyword.keyword_tag.name) for keyword in keywords}
    print("model: ", model)
    model["pycharm"] = "tool"
    return nltk.UnigramTagger(model=model, backoff=None)


tagger = load_dataset()
configuration_weightage()


def retrain_model():
    global tagger
    tagger = load_dataset()


def word_grams(tokens: list) -> list:
    grams = tokens.copy()
    for i in range(1, 7):
        for index in range(len(tokens) - i):
            words = " ".join(tokens[index: index + i + 1])
            grams.append(words)
    return grams


def apply_preprocess(query: str) -> tuple:
    print("query1: ", query)
    skill_list = []
    keywords_record = dict()
    tokens = word_tokenize(query.lower())

    _tokens = [token for token in tokens if token not in stop_words]
    _tokens = word_grams(_tokens)
    # print("tokens: ", _tokens)
    skill_tagger = tagger.tag(_tokens)
    # print("tagger:", skill_tagger)
    for item in skill_tagger:
        if item[1] is None:
            pass
        else:
            skill_list.append(item[0])
            keywords_record[item[0]] = item[1]
    return skill_list, keywords_record


def sentence_extract(data: dict):
    tag_filter = ALTER_KEYWORD_CONFIG['tag_filter']
    category_filter = ALTER_KEYWORD_CONFIG['category_filter']
    exp_weightage = data['weightage']['experience']
    target = dict()
    data_copy = copy.deepcopy(data)
    _requests = data.pop('requests')
    _factors = data.pop('weightage')
    _filters = data.pop('filters')
    queries = _requests[0]['queries']
    print("queries: ", queries)
    queries = copy.deepcopy(queries)
    print("queries: ", queries)
    job_title_score = 0.0

    resume_industry = query_classifier_industry(data)
    queries_result, query_industry = query_industry_classifier(queries, resume_industry,
                                                               EXPERIENCE_WEIGHTAGE.get('relevant_industry', 20))
    industry_status = industry_classifer(query_industry, resume_industry)
    resume_industry.sort(reverse=True)
    most_occur = Counter(resume_industry)
    most_occur = max(most_occur, key=most_occur.get)
    if data["jobTitle"] != "" and _factors['jobTitle'] != 0.0:
        job_title_score = job_title_similarity(data, _factors)
    elif data["jobTitle"] == "":
        job_title_score = _factors['jobTitle'] * 0.5
    experience_sort_order, education_sort_order, certification_sort_order = set(), set(), set()

    for key, value in data.items():
        if isinstance(value, str):
            target[key] = value

        elif isinstance(value, list):
            for instance in value:
                for _key, _value in instance.items():
                    target[f"{key}_{instance['sortOrder']}_{_key}"] = _value
                    if key == "experiences":
                        experience_sort_order.add(instance["sortOrder"])
                    elif key == "educations":
                        education_sort_order.add(instance["sortOrder"])
                    elif key == "certifications":
                        certification_sort_order.add(instance["sortOrder"])

    sorted(experience_sort_order)
    sorted(education_sort_order)
    sorted(certification_sort_order)

    education_score_sum, certification_response = 0, 0
    education_query, certification_query = 0, 0
    qry_no_match = 0
    qry_count = 0
    for request in _requests:
        result = []

        for queries in request["queries"]:

            qry_count += 1
            query = queries["query"]
            _query = query
            if query != "":
                query = re.sub('[^A-Za-z0-9.#+ ]+', '', query)
                print("query2: ", query)
                keywords, keywords_dict = apply_preprocess(query.lower())
                query_status = query_classify(query, CERTIFICATION_WEIGHTAGE['substring_keywords'])
                print("query status: ", query_status)
                temp_keywords = []
                actual_keywords = keywords.copy()
                if _filters['alternativeSkill']:
                    alternatives = []
                    for key, tag in keywords_dict.items():
                        if tag_filter and category_filter:
                            alternatives = KeywordAlternative.objects.filter(
                                actual_keyword_list__keyword_value=key,
                                keyword_tag__name=tag,
                                category=query_status
                            )
                        elif tag_filter:
                            alternatives = KeywordAlternative.objects.filter(
                                actual_keyword_list__keyword_value=key,
                                keyword_tag__name=tag
                            )

                        elif category_filter:
                            alternatives = KeywordAlternative.objects.filter(
                                actual_keyword_list__keyword_value=key,
                                category=query_status
                            )
                    if alternatives:
                        temp_keywords.extend([str(item.alter_keyword_list).split(',') for item in alternatives])

                    keywords.extend(temp_keywords)
                keywords = sorted(set(keywords), key=lambda x: keywords.index(x))
                keywords = list(set(keywords))
                print("keywords: ", keywords)
                sub_result = set()
                if query_status == 'experience':
                    records = KeywordHistory.objects.filter(query=_query)
                    if records.count() > 0:
                        records.update(actual_keywords=",".join(actual_keywords),
                                       alternative_included=",".join(temp_keywords))
                    else:
                        KeywordHistory.objects.create(query=_query, actual_keywords=",".join(actual_keywords),
                                                      alternative_included=",".join(temp_keywords))
                    for i in experience_sort_order:
                        sub_record_exp = dict()
                        target[f"experiences_{i}_description"] = target[f"experiences_{i}_description"].replace(".\n",
                                                                                                                ". ")
                        sentences = target[f"experiences_{i}_description"].lower().split(". ")
                        _sentences = target[f"experiences_{i}_description"].split(". ")

                        for sentence, _sentence in zip(sentences, _sentences):
                            if any(i in sentence for i in keywords):
                                sub_result.add(_sentence + "<br/>")

                        if len(sub_result) != 0:
                            sub_record_exp['jobTitle'] = target[f"experiences_{i}_jobTitle"]
                            sub_record_exp['startDate'] = target[f"experiences_{i}_startDate"]
                            sub_record_exp['endDate'] = target[f"experiences_{i}_endDate"]
                            sub_record_exp['description'] = ".".join(set(sub_result))
                            sub_record_exp['clientName'] = target[f"experiences_{i}_clientName"]
                            sub_record_exp['projectName'] = target[f"experiences_{i}_projectName"]
                            sub_record_exp['tools'] = target[f"experiences_{i}_tools"]
                            result.append(sub_record_exp.copy())

                        sub_result.clear()
                elif query_status == 'education':
                    education_query += 1
                    edu_similarity_score = education_similarity(target, _factors, education_sort_order, query,
                                                                EDUCATION_WEIGHTAGE.get("degree_down_percentage", 80))

                    result.append(data['educations'])
                    education_score_sum += edu_similarity_score
                    result = list(np.concatenate(result))

                elif query_status == 'certification':
                    certification_query += 1
                    certification_sim = certification_similarity(certifications=data["certifications"],
                                                                 filter_w=_factors["certification"], query=_query,
                                                                 certification_weightage_formula=CERTIFICATION_WEIGHTAGE.get('calculation_formula', 20),
                                                                 keywords=keywords)
                    certification_response += certification_sim
                    result.append(data['certifications'])
                    result = list(np.concatenate(result))

                elif query_status == "education_certification":
                    education_query += 1
                    certification_query += 1
                    edu_similarity_score = education_similarity(target, _factors, education_sort_order, query,
                                                                EDUCATION_WEIGHTAGE.get("degree_down_percentage", 80))
                    certification_sim = certification_similarity(certifications=data["certifications"],
                                                                 filter_w=_factors["certification"], query=_query,
                                                                 certification_weightage_formula=CERTIFICATION_WEIGHTAGE.get(
                                                                     'calculation_formula', 20),
                                                                 keywords=keywords)
                    certification_response += certification_sim
                    education_score_sum += edu_similarity_score
                    result.append(data['educations'])
                    result.append(data['certifications'])
                    result = list(np.concatenate(result))

                if len(result) == 0:
                    qry_no_match += 1
                try:
                    record = {
                        "first_name": data['firstName'],
                        "last_name": data['lastName'],
                        "job_title": data['jobTitle'],
                        "query": _query,
                        "predicted_keywords": keywords_dict,
                        "result": "<br>".join(result.copy())
                    }
                    records = ResultHistory.objects.filter(
                        first_name=data['firstName'],
                        last_name=data['lastName'],
                        job_title=data['jobTitle'],
                        query=_query
                    )
                    if records.count() > 0:
                        records.update(**record)
                    elif records.count() == 0:
                        ResultHistory.objects.create(**record)
                except:
                    pass
                queries["result"] = list(result.copy())
                result.clear()
            elif query is None or query == "":
                result.append("No requirements were found for assessment.")
                queries["result"] = list(set(result.copy()))
                result.clear()

    experience_score = 0
    if _factors['experience'] > 0:
        match_count = qry_count - qry_no_match
        query_match_per = (match_count / qry_count) * _factors['experience']
        experience_score = exp_query_similarity(data_copy, EXPERIENCE_WEIGHTAGE.get('query_count', 50))
        experience_score = round((experience_score + query_match_per) / 2, 2)

    qry_per = (sum(queries_result.values()) / len(queries_result.values())) * TOTAL_QUERIES_WEIGHTAGE / 100.0
    final_data = {
        'education': float((education_score_sum / education_query) if education_query > 0 else 0),
        'certification': float(
            (round(certification_response / certification_query, 2)) if certification_query > 0 else 0),
        'experience': round((float(experience_score) + qry_per) / 2, 2),
        'jobTitle': float(job_title_score),
    }
    job_detail = {
        'score': final_data['education'] + final_data['certification'] + final_data['experience'] + final_data[
            'jobTitle'],
        'industry': industry_status,
        'Frequent Industry': most_occur,
        'jobTitle': data['jobTitle']
    }
    return {
        'filters': _filters,
        'jobDetail': job_detail,
        'weightage': final_data,
        'requests': _requests,
    }
