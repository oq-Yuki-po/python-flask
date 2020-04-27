# config.py
import os


class Base(object):
    DB_USER = os.environ.get('POSTGRES_USER')
    DB_PASS = os.environ.get('POSTGRES_PASSWORD')
    DB_URL = os.environ.get('POSTGRES_URL')
    DB_NAME = os.environ.get('POSTGRES_DB')
    DB_PORT = os.environ.get('POSTGRES_PORT', "5432")
    DATABASE = f"postgresql://{DB_USER}:{DB_PASS}@{DB_URL}:{DB_PORT}/{DB_NAME}"


class Development(Base):
    SQL_ECHO = False


class Testing(Base):
    SQL_ECHO = True
