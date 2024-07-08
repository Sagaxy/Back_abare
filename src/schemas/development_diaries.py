from sqlalchemy import Column, Integer, Date, Text, JSON, String, ForeignKey
from models.base import Base

class DevelopmentDiaries(Base):
    __tablename__ = "development-diaries"
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey('child.id'))
    entry_date = Column(Date)
    entry_text = Column(Text)
    title = Column(String)
    detail_treat = Column(JSON)
    assigned_professional_id = Column(Integer, ForeignKey('school-professionals.id'))
    entry_category_tag = Column(String)
