from sqlalchemy import Column, Integer, ForeignKey
from models.base import Base

class DevelopmentDiaryChildDetails(Base):
    __tablename__ = "development-diary-child-details"
    child_id = Column(Integer, ForeignKey('child.id'))
    trait_id = Column(Integer, ForeignKey('traits.id'))
    development_diary_id = Column(Integer, ForeignKey('development-diaries.id'))
