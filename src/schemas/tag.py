from sqlalchemy import Column, Integer, String
from schemas.base import Base

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    value = Column(String)
