from sqlalchemy import Column, Integer, Date, ForeignKey
from schemas.base import Base

class SchoolStudents(Base):
    __tablename__ = "school-students"
    child_id = Column(Integer, ForeignKey('child.id'))
    admission_date = Column(Date)
    school_id = Column(Integer, ForeignKey('schools.id'))
