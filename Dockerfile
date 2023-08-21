# 
FROM python:3.9

# 
WORKDIR /fastAPI_practice

# copy contains from local -> image
COPY ./requirements.txt /fastAPI_practice/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /fastAPI_practice/requirements.txt

# copy contains from local -> image
COPY ./src/ /fastAPI_practice/src/

# copy contains from local -> image
COPY ./data/ /fastAPI_practice/data/

# 
CMD ["uvicorn", "src.app.model_main:app", "--host", "0.0.0.0", "--port", "80"]

# command to build docker image
# docker build -t movie_sentiment_analysis .

# command to run docker image
# docker run -p 80:80 movie_sentiment_analysis

# to see the fastapi interface, go docker desktop