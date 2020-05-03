from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.models.setting import Engine, BaseModel
from database.models import File


class FileDetail(BaseModel):
    """
    FileDetailModel
    """
    __tablename__ = 'file_details'

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_id = Column(Integer, ForeignKey(File.id), nullable=False)
    row = Column(Integer, nullable=False)
    contents = Column(String(255), nullable=False)
    file = relationship('File', backref="file_details")

    def __init__(self, file, row, contents, created_at=None, updated_at=None):
        self.file = file
        self.row = row
        self.contents = contents
        self.created_at = created_at
        self.updated_at = updated_at


if __name__ == "__main__":
    BaseModel.metadata.create_all(bind=Engine)
