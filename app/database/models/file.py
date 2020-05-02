from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.models.setting import Engine, ModelBase
from database.models import User


class File(ModelBase):
    """
    FileModel
    """
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(User.id))
    name = Column(String(255), nullable=False)
    user = relationship('User', backref="files")

    def __init__(self, user, name, created_at=None, updated_at=None):
        self.users = user
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at


if __name__ == "__main__":
    ModelBase.metadata.create_all(bind=Engine)
