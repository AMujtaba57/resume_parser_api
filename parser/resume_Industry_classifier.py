import os
import pickle
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle

from api.models import ResumeDescriptionDataset
from core.settings import MODEL_ROOT


def load_industry_dataset():
    resume_dataset = ResumeDescriptionDataset.objects.all()
    model = [{"label": item.industry.industry_label, "des": item.industry_definition} for item in
             resume_dataset]
    if resume_dataset.count() == 0:
        model['label'] = 'it'
        model[
            'des'] = 'Consulted within the IT organization to develop appropriate support for IT centric projects from ' \
                     'various technology and service departments; integrate activities with business units, ' \
                     'corporate departments, and IT departments to ensure the successful implementation and support of ' \
                     'project efforts. \n Managed the project deliverables by using Agile and SPRINT development ' \
                     'model, managed the day to day assignments, and verified of work done by resources. \n Managed ' \
                     'daily ' \
                     'SCRUM meetings and biweekly SPRINT meetings. \n Performed the code review, and measured the ' \
                     'quality matrices. \n Made sure that team members successfully customized the DevExpress and ' \
                     'XtraReports library to integrate Needles report objects to provide complete solution for ' \
                     'on-demand reports building. \n Achieved a complete solution without requiring any design or ' \
                     'specifications documents. '
    df = pd.DataFrame(model)
    return df


def process_dataset(df):
    corpus = df['des'].values
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


def _model_training_rfc(train_x, train_y):
    randomForestClassifier = RandomForestClassifier()
    randomForestClassifier.fit(train_x, train_y)
    return randomForestClassifier


def save_model(model, vectorizer):
    pickle.dump(model, open(os.path.join(MODEL_ROOT, 'industry_description_classifier.pkl'), 'wb'))
    joblib.dump(vectorizer, os.path.join(MODEL_ROOT, 'industry_description_vectorizer.joblib'))


def retrain_industry_model():
    df = load_industry_dataset()
    if df.shape[0] > 10:
        train_x, train_y, label_encoder, vectorizer = process_dataset(df)
        model = _model_training_rfc(train_x, train_y)
        save_model(model, vectorizer)


def query_classifier_industry(data):
    industry_list = []
    label_encoder = pickle.load(open(os.path.join(MODEL_ROOT, 'label_encoder_classes.pkl'), 'rb'))

    for i in range(0, len(data['experiences'])):
        text = data['experiences'][i]['description'].lower()
        dataframe = pd.DataFrame([[text]], columns=['des'])
        corpus = dataframe['des'].values

        classifier = pickle.load(open(os.path.join(MODEL_ROOT, 'industry_description_classifier.pkl'), 'rb'))
        feature_vectorizer = joblib.load(os.path.join(MODEL_ROOT, 'industry_description_vectorizer.joblib'))
        X = feature_vectorizer.transform(corpus)
        feature_name = pd.DataFrame(X.toarray(), columns=feature_vectorizer.get_feature_names_out())
        model_prediction = classifier.predict(feature_name)

        label = label_encoder.inverse_transform(model_prediction)
        industry_list.append(label[0])
    return industry_list
