from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.models.setting import ENGINE
from database.models.base import DefaultBase
from database.models import File


class FileDetail(DefaultBase):
    """
    FileDetailModel
    """
    __tablename__ = 'file_details'

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_id = Column(Integer, ForeignKey(File.id))
    row = Column(Integer)
    contents = Column(String(255))
    files = relationship('File')

    def __init__(self, files, row, contents, created_at, updated_at):
        super().__init__(created_at, updated_at)
        self.files = files
        self.row = row
        self.contents = contents


if __name__ == "__main__":
    DefaultBase.metadata.create_all(bind=ENGINE)
