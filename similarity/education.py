import warnings

import pandas as pd
import spacy
from nltk.tokenize import word_tokenize

from api.models import EducationLevels

nlp = spacy.load('en_core_web_sm')

warnings.filterwarnings("ignore", category=DeprecationWarning)

level_list = None
education_list = None
education_level = None


def load_dataset():
    model = {}
    try:
        levels = EducationLevels.objects.all()
        model = {str(keyword.name).lower(): str(keyword.level) for keyword in levels}
    except:
        model["matric"] = 0
    return model


def retrain_model():
    global level_list, education_list, education_level
    education_level = load_dataset()
    education_list = [key.lower() for key, value in education_level.items()]
    level_list = [int(value) for key, value in education_level.items()]


retrain_model()


def word_grams(tokens: list) -> list:
    grams = tokens.copy()
    for index in range(len(tokens) - 1):
        words = " ".join(tokens[index: index + 2])
        grams.append(words)

    for index in range(len(tokens) - 2):
        words = " ".join(tokens[index: index + 3])
        grams.append(words)
    return grams


def extract_education(resume_text):
    token_word = word_tokenize(resume_text)
    token_word = word_grams(token_word)
    for word in token_word:
        if word in education_list:
            return word


def query_classify(query, substring_keyword):
    status = ''
    query = query.lower()

    edu = [edu for edu in education_list if edu in query]
    cert = [certi for certi in substring_keyword if certi in query]

    if len(edu) > 0 and len(cert) == 0:
        status = "education"
    elif len(edu) == 0 and len(cert) > 0:
        status = 'certification'
    elif len(edu) > 0 and len(cert) > 0:
        status = 'education_certification'
    else:
        status = 'experience'
    return status


def education_similarity(target, _factors, education_sort_order, query, education_weightage):
    try:
        query_education = ""
        query = query.lower()
        sorted_level_list = sorted(list(set(level_list)), reverse=True)
        for education in education_list:
            if query.find(education) >= 0:
                query_education = education
        query_education_level = int((pd.Series(query_education)).map(education_level))
        education, _sum = {}, []
        for i in education_sort_order:
            if target[f"educations_{i}_degreeName"] != '':
                text_lower = target[f"educations_{i}_degreeName"].lower()
                clean_text = extract_education(text_lower)
                resource_education_level = int((pd.Series(clean_text)).map(education_level))
                education[text_lower] = resource_education_level

        for value in sorted(education.values()):
            resume_education_index = sorted_level_list.index(value)
            query_education_index = sorted_level_list.index(query_education_level)
            if query_education_level > value:
                weightage = (float(_factors['education']) - (
                        (education_weightage / 100) * float(
                    _factors['education'])) * (resume_education_index - query_education_index))
            else:
                weightage = _factors['education']

            _sum.append(weightage)
        return max(_sum)
    except Exception:
        _sum = 0
        return _sum
