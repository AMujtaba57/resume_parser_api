import math

import spacy

from api.models import EducationLevels

nlp = spacy.load('en_core_web_sm')
import nltk
import warnings
from nltk.tokenize import word_tokenize

warnings.filterwarnings("ignore", category=DeprecationWarning)
try:
    from nltk.corpus import stopwords

    stop_words = set(stopwords.words("english"))
except Exception:
    nltk.download("stopwords")
    from nltk.corpus import stopwords

    stop_words = set(stopwords.words("english"))
from nltk.stem import PorterStemmer


def load_dataset():
    model = {}
    try:
        levels = EducationLevels.objects.all()
        model = {str(keyword.name).lower(): str(keyword.level) for keyword in levels}
    except:
        # model["matric"] = 0
        pass
    return model


def retrain_model():
    global tagger
    return load_dataset()


ps = PorterStemmer()

education_level = retrain_model()
education_list = [key.lower() for key, value in education_level.items()]


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


def education_similarity(target, _factors, education_sort_order, certification_sort_order):
    response = dict()
    for key, value in _factors.items():
        weightage = 0
        if key == 'education':
            try:
                sentence = _factors[key]['name'].lower()
                education_index = extract_education(sentence)
                required_index = int((pd.Series(education_index)).map(education_level))
                if required_index is not None:
                    tokens = word_tokenize(sentence)
                    _tokens = [token for token in tokens if token not in stop_words]
                    _tokens = word_grams(_tokens)
                    for i in education_sort_order:
                        weightage = 0
                        if target[f"educations_{i}_degreeName"] != '':
                            text_lower = target[f"educations_{i}_degreeName"].lower()
                            clean_text = extract_education(text_lower)
                            resource_index = int((pd.Series(clean_text)).map(education_level))
                            if resource_index is not None:
                                if resource_index >= required_index:
                                    weightage = _factors[key]['weightage']
                                else:
                                    if required_index - resource_index == 1:
                                        weightage = math.ceil(_factors[key]['weightage'] / 2)
                                    elif required_index - resource_index == 2:
                                        weightage = math.ceil(_factors[key]['weightage'] / 5)
                        else:
                            weightage = 0
                response[key] = weightage
            except Exception as e:
                response[key] = "Invalid Input"

        if key == 'certification':
            obj_sum = 0
            sentence = _factors[key]['names'].lower()
            tokens = word_tokenize(sentence)
            _tokens = [token for token in tokens if token not in stop_words]
            for i in certification_sort_order:
                if target[f"certifications_{i}_name"] != '':
                    sum = 0
                    resource_list = target[f"certifications_{i}_name"].split(' ')
                    if len(_tokens) <= len(resource_list):
                        for item in resource_list:
                            if item.lower() in _tokens:
                                sum += 1 / len(resource_list)
                    else:
                        for word in _tokens:
                            if word in list(map(str.lower, resource_list)):
                                sum += 1 / len(_tokens)
                    obj_sum += sum
            response[key] = math.ceil(
                float("%.2f" % ((obj_sum / len(certification_sort_order)) * _factors[key]['weightage'])))
    return response
