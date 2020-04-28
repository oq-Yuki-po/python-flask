from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.setting import ENGINE
from database.models.base import DefaultBase


class File(DefaultBase):
    """
    FileModel
    """
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String(255))
    users = relationship('User', backref="files")

    def __init__(self, users, name, created_at, updated_at):
        super().__init__(created_at, updated_at)
        self.users = users
        self.name = name


if __name__ == "__main__":
    DefaultBase.metadata.create_all(bind=ENGINE)
