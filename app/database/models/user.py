from sqlalchemy import Column, String, Integer

from database.models.setting import Engine, BaseModel


class User(BaseModel):
    """
    UserModel
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)

    def __init__(self, name, created_at=None, updated_at=None):
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at


if __name__ == "__main__":
    BaseModel.metadata.create_all(bind=Engine)
