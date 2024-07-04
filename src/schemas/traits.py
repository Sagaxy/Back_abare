from sqlalchemy import Column, Integer, Boolean, String, ForeignKey
from schemas.base import Base

class Traits(Base):
    __tablename__ = "traits"
    id = Column(Integer, primary_key=True)
    isvalid = Column(Boolean)
    value = Column(String)
    child_id = Column(Integer, ForeignKey('child.id'))
    tag_id = Column(Integer, ForeignKey('tags.id'))
