from datetime import datetime
from sqlalchemy import (Column, String, ForeignKey, Integer, DateTime)

from database.setting import ENGINE, DB_Base


class DefaultBase(DB_Base):
    """
    DefaultBase
    """
    __abstract__ = True
    
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False)
    