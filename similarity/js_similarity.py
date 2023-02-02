import json
import re
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from api.models import Configuration
from parser.experience import get_total_experience
from parser.exp_validator import extract_exp
import textdistance as td


def _base_clean(text):
    """
    Takes in text read and then does the text cleaning.
    """
    text = tokenize(text)
    text = remove_stopwords(text)
    text = remove_tags(text)
    text = lemmatize(text)
    return text


def _reduce_redundancy(text):
    """
    Takes in text that has been cleaned by the _base_clean and uses set to reduce the repeating words
    giving only a single word that is needed.
    """
    return list(set(text))


def _get_target_words(text):
    """
    Takes in text and uses Spacy Tags on it, to extract the relevant Noun, Proper Noun words that contain words
    related to tech and JD.
    """
    target = []
    sent = " ".join(text)
    doc = nlp(sent)
    for token in doc:
        if token.tag_ in ['NN', 'NNP']:
            target.append(token.text)
    return target


def Cleaner(text):
    sentence = []
    sentence_cleaned = _base_clean(text)
    sentence.append(sentence_cleaned)
    sentence_reduced = _reduce_redundancy(sentence_cleaned)
    sentence.append(sentence_reduced)
    sentence_targetted = _get_target_words(sentence_reduced)
    sentence.append(sentence_targetted)
    return sentence


stop_words = stopwords.words('english')

nlp = spacy.load('en_core_web_sm')


def remove_stopwords(text, sw=stop_words, optional_params=False, optional_words=None):
    if optional_words is None:
        optional_words = []
    if optional_params:
        sw.append([a for a in optional_words])
    return [word for word in text if word not in sw]


def tokenize(text):
    text = re.sub(r'[^\w\s]', '', text)
    return word_tokenize(text)


def lemmatize(text):
    # the input to this function is a list
    str_text = nlp(" ".join(text))
    lemmatized_text = []
    for word in str_text:
        lemmatized_text.append(word.lemma_)
    return lemmatized_text


def _to_string(List):
    # the input parameter must be a list
    string = " "
    return string.join(List)


def remove_tags(text, postags=None):
    """
    Takes in Tags which are allowed by the user and then eliminates the rest of the words
    based on their Part of Speech (POS) Tags.
    """
    if postags is None:
        postags = ['PROPN', 'NOUN', 'ADJ', 'VERB', 'ADV']
    filtered = []
    str_text = nlp(" ".join(text))
    for token in str_text:
        if token.pos_ in postags:
            filtered.append(token.text)
    return filtered


def match(candidate_data, original_data, exp_weightage):
    j = td.jaccard.similarity(candidate_data, original_data)
    s = td.sorensen_dice.similarity(candidate_data, original_data)
    c = td.cosine.similarity(candidate_data, original_data)
    o = td.overlap.normalized_similarity(candidate_data, original_data)
    total = (j + s + c + o) / 4
    # total = (s+o)/2
    return total * (exp_weightage / 100)


def jd_similarity(data):
    """
    Parameters:
        data (dict): Takes in input as json format as a request.
    Returns:
        similarity (float): Provides the output of similarity percentage between job
        description and experience.
    """
    factor = data['factor']
    jd = factor['work_experience']
    jd_weightage = jd['weightage']
    original = jd['description']
    experiences = data['experiences']
    candidate = ''
    for exp in experiences:
        candidate += exp['description']

    cleaned_candidate_data = Cleaner(candidate)
    cleaned_original_data = Cleaner(original)

    original_set = set(cleaned_original_data[2])
    candidate_set = set(cleaned_candidate_data[2])

    intersection = original_set.intersection(candidate_set)
    original_count = len(original_set)
    intersection_count = len(intersection)
    similarity = round((intersection_count / original_count * jd_weightage), 2)

    return similarity


def exp_query_similarity(data, experience_weightage):
    """
    Parameters:
        data (dict): Takes in input as json format as a request.
    Returns:
        similarity (float): Provides the output of similarity percentage between job
        description and experience.
    """
    exp_weightage = experience_weightage  # New Scoring
    queries_data = data['requests']
    mm_l = []
    candidate = ''
    experiences = data['experiences']
    general_exp, ral_exp = get_total_experience(data)
    match_required_experience = []
    max_exp = 1
    for exp in experiences:
        candidate += exp['description']
    for queries_dict in queries_data:

        queries = queries_dict['queries']

        for query in queries:
            original = query['query']

            # -------- Comparing Experience with Query ----------- #

            exp_need = extract_exp(original)
            exp_type = check_exp_type(exp_need)

            exp_no = [int(e) for e in exp_need.split() if e.isdigit()]

            if len(exp_no) == 0:
                exp_no.append(0)

            if max_exp < exp_no[0]:
                max_exp = exp_no[0]
            for job_title in ral_exp.keys():
                sk_list = ral_exp[job_title]['skills']
                sk_list = sk_list[0]
                if any([sk for sk in sk_list if sk in original]):
                    if exp_type == 0 or exp_type == 1:
                        if ral_exp[job_title]['experience'] >= exp_no[0]:
                            match_required_experience.append(exp_weightage)
                        else:
                            match_required_experience.append(exp_weightage / 4)
                        break
                    elif exp_type == 2 or exp_type == 3 or exp_type == 5:
                        if ral_exp[job_title]['experience'] <= exp_no[0]:
                            match_required_experience.append(exp_weightage)
                        else:
                            match_required_experience.append(exp_weightage / 4)
                        break
                    elif exp_type == 3:
                        if ral_exp[job_title]['experience'] == exp_no[0]:
                            match_required_experience.append(exp_weightage)
                        else:
                            match_required_experience.append(exp_weightage / 4)

            cleaned_candidate_data = Cleaner(candidate)
            cleaned_original_data = Cleaner(original)
            original_set = cleaned_original_data[2]
            candidate_set = cleaned_candidate_data[2]
            mm = match(candidate_set, original_set, experience_weightage) * exp_weightage
            mm_l.append(mm)

    # Relevant Experience Matching
    if len(match_required_experience) != 0:
        match_exp_per = (sum(match_required_experience) / len(match_required_experience)) * exp_weightage
    else:
        match_exp_per = 0
    if match_exp_per > exp_weightage:
        match_exp_per = exp_weightage

    exp_simi = round(sum(mm_l), 2)

    exp_simi /= len(mm_l)

    if exp_simi > exp_weightage:
        exp_simi = exp_weightage

    general_exp_per = (general_exp / max_exp) * exp_weightage

    if general_exp_per > exp_weightage:
        general_exp_per = exp_weightage

    total_exp = (match_exp_per + exp_simi + general_exp_per) / 3

    return round(total_exp, 2)


def check_exp_type(extracted_exp):
    if 'minimum' in extracted_exp:
        return 0
    if 'least' in extracted_exp:
        return 1
    if 'over' in extracted_exp:
        return 2
    if 'maximum' in extracted_exp:
        return 3
    if 'equal' in extracted_exp:
        return 4
    if 'most' in extracted_exp:
        return 5
    return 6

