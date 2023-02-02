import json
import os
import pickle
import warnings
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle

from api.models import QueryIndustryDataset, Configuration
from core.settings import MODEL_ROOT

warnings.filterwarnings("ignore")


def load_query_dataset():
    query_dataset = QueryIndustryDataset.objects.all()
    model = [{"query": item.query, "label": item.industry.industry_label} for item in
             query_dataset]
    if query_dataset.count() == 0:
        model['label'] = 'it'
        model['query'] = 'Experience participating in the development and testing of applications on Amazon Web' \
                         ' Services (AWS), Microsoft Azure, Force.com, and/or Google Cloud Platforms. Experience in ' \
                         'running large, complicated IT application designs, developments, and implementations.'

    df = pd.DataFrame(model)
    return df


def process_dataset(df):
    corpus = df['query'].values
    vectorizer = TfidfVectorizer(ngram_range=(1, 1), analyzer='word', max_features=100, )
    X = vectorizer.fit_transform(corpus)
    column = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

    dataframe = pd.concat([column, df['label']], axis=1)
    s_data = shuffle(dataframe)
    label_encoder = LabelEncoder()
    encoded_labels = label_encoder.fit_transform(s_data['label'])
    pickle.dump(label_encoder, open(os.path.join(MODEL_ROOT, 'label_encoder_classes.pkl'), 'wb'))
    s_data.insert(s_data.shape[1], "encoded industry", encoded_labels)
    s_data['label'] = s_data['encoded industry']
    del (s_data['encoded industry'])

    train_x = s_data.values[:, :-1]
    train_y = s_data["label"].values

    return train_x, train_y, label_encoder, vectorizer


def _model_training_rfc(train_X, train_Y):
    randomForestClassifier = RandomForestClassifier()
    randomForestClassifier.fit(train_X, train_Y)
    return randomForestClassifier


def save_model(model, vectorizer):
    pickle.dump(model, open(os.path.join(MODEL_ROOT, 'industry_description_classifier.pkl'), 'wb'))
    joblib.dump(vectorizer, os.path.join(MODEL_ROOT, 'industry_description_vectorizer.joblib'))


def retrain_query_model():

    df = load_query_dataset()
    if df.shape[0] > 10:
        train_x, train_y, label_encoder, vectorizer = process_dataset(df)
        model = _model_training_rfc(train_x, train_y)
        save_model(model, vectorizer)


def query_industry_classifier(queries, industry_description, expe_weightage):
    label_encoder = pickle.load(open(os.path.join(MODEL_ROOT, 'label_encoder_classes.pkl'), 'rb'))
    query_weightage, industry_set = {}, set()
    for qry in queries:
        text = qry['query']
        dataframe = pd.DataFrame([[text]], columns=['query'])
        corpus = dataframe['query'].values

        classifier = pickle.load(open(os.path.join(MODEL_ROOT, 'industry_query_classifier.pkl'), 'rb'))
        feature_vectorizer = joblib.load(os.path.join(MODEL_ROOT, 'industry_query_vectorizer.joblib'))
        X = feature_vectorizer.transform(corpus)
        feature_name = pd.DataFrame(X.toarray(), columns=feature_vectorizer.get_feature_names_out())
        model_prediction = classifier.predict(feature_name)

        label = label_encoder.inverse_transform(model_prediction)
        if label[0] in industry_description:
            query_weightage[qry['sortOrder']] = expe_weightage
        else:
            query_weightage[qry['sortOrder']] = 0
        industry_set.add(label[0])
    return query_weightage, industry_set
