from sqlalchemy import Column, Integer, ForeignKey
from schemas.base import Base

class FamilyChildren(Base):
    __tablename__ = "family-children"
    child_id = Column(Integer, ForeignKey('child.id'))
    family_id = Column(Integer, ForeignKey('family.id'))
