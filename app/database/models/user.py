from sqlalchemy import Column, String, Integer

from database.models.setting import ENGINE
from database.models.base import DefaultBase


class User(DefaultBase):
    """
    UserModel
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))

    def __init__(self, name, created_at, updated_at):
        super().__init__(created_at, updated_at)
        self.name = name


if __name__ == "__main__":
    DefaultBase.metadata.create_all(bind=ENGINE)
