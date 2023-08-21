# general imports
import numpy as np
import pandas as pd
import os
import sys

# Data Preprocessing
from imblearn.under_sampling import RandomUnderSampler

# Train test split
from sklearn.model_selection import train_test_split

# Text Representation (BOW)
from sklearn.feature_extraction.text import TfidfVectorizer

# Model training
from sklearn.svm import SVC

# save model:
import pickle


def read_data(file_path: str):
    return pd.read_csv(file_path)


# Preprocessing
def data_preprocessing(df: pd.DataFrame):
    rus = RandomUnderSampler(random_state=0)
    df_review_bal, df_review_bal["sentiment"] = rus.fit_resample(
        df[["review"]], df["sentiment"]
    )
    # reduce training data to 10%
    df_review_bal_throw, df_review_bal = train_test_split(
        df, test_size=0.10, random_state=42
    )
    return df_review_bal


# Train test split
def data_split(df: pd.DataFrame):
    train, test = train_test_split(df, test_size=0.33, random_state=42)
    train_x, train_y = train["review"], train["sentiment"]
    test_x, test_y = test["review"], test["sentiment"]
    return train_x, train_y, test_x, test_y


def data_vectorizer(train_x, test_x):
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf.fit(train_x)
    train_x_vector = tfidf.transform(train_x)
    # also transform the test_x_vector
    test_x_vector = tfidf.transform(test_x)
    return train_x_vector, test_x_vector, tfidf


def svm_model_train(train_x_vector, train_y):
    svc = SVC(kernel="linear")
    svc.fit(train_x_vector, train_y)
    return svc


def input_prediction(svc, tfidf, input: str):
    # tfidf = TfidfVectorizer(stop_words="english")
    return svc.predict(tfidf.transform([input]))


def model_prediction(svc, test_x_vector, test_y):
    return svc.score(test_x_vector, test_y)  # accuacry


def save_model(svc, file_path: str):
    with open(file_path, "wb") as file:
        pickle.dump(svc, file)


# run pipeline here
# current_script_path = os.path.abspath(__file__)
# parent_directory = os.path.dirname(current_script_path)
# parent_directory = os.path.dirname(parent_directory)  # src
# parent_parent_directory = os.path.dirname(parent_directory)  # fastAPI_practice/
# file_path = os.path.join(parent_parent_directory, "data", "01_raw", "IMDB_Dataset.csv")
# file_path_model = os.path.join(
#     parent_parent_directory, "data", "02_saved_model", "model.pkl"
# )
# file_path_vectorizer = os.path.join(
#     parent_parent_directory, "data", "02_saved_model", "vectorizer.pkl"
# )

# df = read_data(file_path)
# df_review_bal = data_preprocessing(df)
# train_x, train_y, test_x, test_y = data_split(df_review_bal)
# train_x_vector, test_x_vector, tfidf = data_vectorizer(train_x, test_x)
# print("training model")
# svc = svm_model_train(train_x_vector, train_y)
# print("model training completed")
# print(input_prediction(svc, tfidf, "A good movie"))
# save_model(tfidf, file_path_vectorizer)
# save_model(svc, file_path_model)

# with open(file_path_vectorizer, "rb") as vectorizer_file:
#     tfidf = pickle.load(vectorizer_file)

# with open(file_path_model, "rb") as model_file:
#     model = pickle.load(model_file)
# print(input_prediction(model, tfidf, "This is a great movie")[0])
# print(f"saving model weights to {file_path_model}")
# save_model(svc, file_path_model)
# save_model(tfidf, file_path_vectorizer)  # save vectorizer
