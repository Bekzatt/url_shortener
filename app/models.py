"""
SQLAlchemy модели для хранения сокращённых URL в базе данных.
"""

from sqlalchemy import Column, String, Integer
from database import Base

class ShortURL(Base):
    __tablename__ = "short_urls"

    id = Column(Integer, primary_key=True, index=True)
    short_id = Column(String,nullable=False)
    original_url = Column(String, nullable=False)
