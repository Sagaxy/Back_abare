from sqlalchemy import Column, Integer, String, ForeignKey
from schemas.base import Base

class SchoolProfessionals(Base):
    __tablename__ = "school-professionals"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    role = Column(String)
    cpf = Column(String)
    address = Column(String)
    school_id = Column(Integer, ForeignKey('schools.id'))
