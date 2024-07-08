from sqlalchemy import Column, Integer, String, Date, ForeignKey
from models.base import Base

class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    picture = Column(String)
    birth_date = Column(Date)
    gender = Column(String)
    spectrum_degree = Column(String)
    trait_id = Column(String, ForeignKey('traits.id'))
