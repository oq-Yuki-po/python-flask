from sqlalchemy import Column, String, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship

from database.setting import ENGINE
from database.models.base import DefaultBase
from database.models import File


class FileDetail(DefaultBase):
    """
    FileDetailModel
    """
    __tablename__ = 'file_details'
    id = Column(Integer, primary_key=True, autoincrement=True)
    file_id = Column(Integer, ForeignKey('files.id'))
    row = Column(Integer)
    contents = Column(String(255)) 
    files = relationship('File', backref="file_details")

    def __init__(self, file_id, row, contents):
        self.file_id = file_id
        self.row = row
        self.contents = contents

if __name__ == "__main__":
    DefaultBase.metadata.create_all(bind=ENGINE)
