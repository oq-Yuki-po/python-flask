# build command 
# docker build --pull --rm -f ".docker/develop/Dockerfile" -t flask-python:develop .

FROM python:3.8.2-slim

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    build-essential \
    python-dev \
    libpq-dev \
    postgresql

RUN pip install poetry

WORKDIR /usr/src/flask/app

COPY app/poetry.lock app/pyproject.toml ./

RUN poetry config virtualenvs.create false \
    && poetry install

ENV PYTHONPATH "${PYTHONPATH}:/usr/src/flask/app"

CMD ["uwsgi","--ini","uwsgi.ini"]