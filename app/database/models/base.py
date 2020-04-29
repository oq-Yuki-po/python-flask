import os
from datetime import datetime
from sqlalchemy import Column, DateTime

from database.setting import DB_Base


class DefaultBase(DB_Base):
    """
    DefaultBase
    """
    __abstract__ = True
    __table_args__ = {'schema' : os.environ.get('DB_SCHEMA', None) }

    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False)

    def __init__(self, created_at, updated_at):
        self.created_at = created_at
        self.updated_at = updated_at
