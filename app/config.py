# config.py
import os
import logging


class BaseConfig(object):
    API_VERSION = '/v1'
    DB_USER = os.environ.get('POSTGRES_USER')
    DB_PASS = os.environ.get('POSTGRES_PASSWORD')
    DB_URL = os.environ.get('POSTGRES_URL')
    DB_NAME = os.environ.get('POSTGRES_DB')
    DB_PORT = os.environ.get('POSTGRES_PORT', "5432")
    DATABASE = f"postgresql://{DB_USER}:{DB_PASS}@{DB_URL}:{DB_PORT}/{DB_NAME}"
    JSON_AS_ASCII = False
    RESTFUL_JSON = {
        'ensure_ascii': False
    }


class Development(BaseConfig):
    SQL_ECHO = False
    LOG_LEVEL = logging.INFO


class Testing(BaseConfig):
    SQL_ECHO = True
    LOG_LEVEL = logging.DEBUG
