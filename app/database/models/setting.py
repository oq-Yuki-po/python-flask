from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy_utils import database_exists, create_database

from config import Base
from api.responses.errors import DataBaseConnecitonError


def initialize_db():
    try:
        engine = create_engine(Base.DATABASE)
        if not database_exists(engine.url):
            create_database(engine.url)
    except SQLAlchemyError:
        raise DataBaseConnecitonError()


Engine = create_engine(
    Base.DATABASE,
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

DB_Base = declarative_base()
