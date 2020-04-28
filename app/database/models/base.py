from datetime import datetime
from sqlalchemy import Column, DateTime

from database.setting import DB_Base


class DefaultBase(DB_Base):
    """
    DefaultBase
    """
    __abstract__ = True

    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False)

    def __init__(self, created_at, updated_at):
        self.created_at = created_at
        self.updated_at = updated_at
