# build command 
# docker build --pull --rm -f ".docker/product/Dockerfile" -t python-flask:product .

FROM python:3.8.2-slim

RUN apt-get update \
    && apt-get upgrade -y

RUN pip install poetry

WORKDIR /usr/src/app

COPY app ./

RUN poetry config virtualenvs.create false \
    && poetry install