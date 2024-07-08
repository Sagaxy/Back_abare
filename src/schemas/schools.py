from sqlalchemy import Column, Integer, String
from schemas.base import Base

class Schools(Base):
    __tablename__ = "schools"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    contact_email = Column(String)
    contact_telephone = Column(String)
