from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from database.setting import ENGINE
from database.models.ModelBase import DefaultBase


class User(DefaultBase):
    """
    FileModel
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))

    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    DefaultBase.metadata.create_all(bind=ENGINE)
