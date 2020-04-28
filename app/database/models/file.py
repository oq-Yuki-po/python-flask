from sqlalchemy import Column, String, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship

from database.setting import ENGINE
from database.models.base import DefaultBase
from database.models.user import User


class File(DefaultBase):
    """
    FileModel
    """
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String(255))
    users = relationship('User', backref="files")

    def __init__(self, users, name):
        self.users = users
        self.name = name


if __name__ == "__main__":
    DefaultBase.metadata.create_all(bind=ENGINE)
