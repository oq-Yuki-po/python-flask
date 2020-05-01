from sqlalchemy import Column, String, Integer

from database.models.setting import Engine, ModelBase


class User(ModelBase):
    """
    UserModel
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))

    def __init__(self, name, created_at, updated_at):
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at


if __name__ == "__main__":
    ModelBase.metadata.create_all(bind=Engine)
