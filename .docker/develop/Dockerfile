# build command 
# docker build --pull --rm -f ".docker/develop/Dockerfile" -t flask-python:develop .

FROM python:3.8.2-slim

RUN apt-get update \
    && apt-get upgrade -y

RUN pip install poetry

WORKDIR /usr/src/app

COPY app/poetry.lock app/pyproject.toml ./

RUN poetry config virtualenvs.create false \
    && poetry install