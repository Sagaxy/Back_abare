from sqlalchemy import Column, Integer, ForeignKey
from schemas.base import Base

class SchoolAdministrators(Base):
    __tablename__ = "school-administrators"
    id = Column(Integer, primary_key=True)
    admin_user_id = Column(Integer, ForeignKey('users.id'))
    school_id = Column(Integer, ForeignKey('schools.id'))
