from sqlalchemy import Column, Integer
from schemas.base import Base

class Family(Base):
    __tablename__ = "family"
    id = Column(Integer, primary_key=True)
    emergence_contact_id = Column(Integer)
