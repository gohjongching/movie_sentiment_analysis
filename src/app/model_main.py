from fastapi import FastAPI
from pydantic import BaseModel

import sys
import pickle
import os

# load the model:
current_script_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(current_script_path)
parent_directory = os.path.dirname(parent_directory)  # src
path_to_function = os.path.join(parent_directory, "model_training_pipeline")
sys.path.append(path_to_function)

from training_pipeline import input_prediction

parent_parent_directory = os.path.dirname(parent_directory)  # fastAPI_practice/
file_path_model = os.path.join(
    parent_parent_directory, "data", "02_saved_model", "model.pkl"
)
file_path_vectorizer = os.path.join(
    parent_parent_directory, "data", "02_saved_model", "vectorizer.pkl"
)

# Load the TF-IDF vectorizer and the trained model
with open(file_path_model, "rb") as file:
    model = pickle.load(file)

with open(file_path_vectorizer, "rb") as file:
    tfidf = pickle.load(file)


class my_input(BaseModel):
    movie_review_input: str


app = FastAPI()


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": "0.1"}


@app.post("/predict/")
async def main(input: my_input):
    movie_review = input.dict()
    movie_review_str = movie_review["movie_review_input"]
    prediction = input_prediction(model, tfidf, movie_review_str)
    return {"Sentiment Analysis of review input": prediction[0]}
