from sqlalchemy import Column, Integer, Date, ForeignKey
from schemas.base import Base

class SchoolProfessionalAssignments(Base):
    __tablename__ = "school-professional-assignments"
    professional_id = Column(Integer, ForeignKey('school-professionals.id'))
    employment_date = Column(Date)
    school_id = Column(Integer, ForeignKey('schools.id'))
