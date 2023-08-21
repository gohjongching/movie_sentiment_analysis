# Problem Statement: Movie Sentiment Analysis for Improving User Experience

## Background:
In today's digital age, movies are widely consumed across various platforms, including theaters, streaming services, and television. Understanding how viewers perceive movies is essential for movie producers, studios, and streaming platforms to make informed decisions about content creation, marketing strategies, and user engagement. Sentiment analysis, a subfield of natural language processing (NLP), offers a valuable tool to gain insights into viewers' opinions and sentiments related to movies.

## Problem:
The problem at hand is to develop a sentiment analysis system that can automatically determine the sentiment expressed in movie reviews or comments. The sentiment could be positive, negative, or neutral. The goal is to create a model that accurately classifies the sentiment of a given text review, contributing to better understanding viewer preferences and enhancing user experience.

## Pipeline
### Model and vectorizer used

## To build docker image for inference with Fastapi for model serving
`docker build -t movie_sentiment_analysis .`

## run docker image for inference 
`docker run -p 80:80 movie_sentiment_analysis`

## How to run Fastapi, post request