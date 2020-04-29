from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from config import Base


def initialize_db():
    engine = create_engine(Base.DATABASE)
    if not database_exists(engine.url):
        create_database(engine.url)


ENGINE = create_engine(
    Base.DATABASE,
    encoding="utf-8",
    echo=True
)

session = scoped_session(
    # ORM実行時の設定。自動コミットするか、自動反映するなど。
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

DB_Base = declarative_base()
