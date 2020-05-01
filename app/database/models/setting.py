import os
from datetime import datetime

from sqlalchemy import create_engine, Column, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy_utils import database_exists, create_database

from config import BaseConfig
from api.responses.errors import DataBaseConnecitonError


def initialize_db():
    try:
        engine = create_engine(BaseConfig.DATABASE)
        if not database_exists(engine.url):
            create_database(engine.url)
    except SQLAlchemyError:
        raise DataBaseConnecitonError()


Engine = create_engine(
    BaseConfig.DATABASE,
    encoding="utf-8",
    echo=False
)

Session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=Engine
    )
)

class Base(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __table_args__ = {'schema': os.environ.get('DB_SCHEMA', None)}

    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False)

ModelBase = declarative_base(cls=Base)
