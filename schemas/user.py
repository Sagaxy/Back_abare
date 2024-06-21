from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, JSON, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    adress = Column(String)
    phone = Column(String)
    access = Column(Integer)

class Family(Base):
    __tablename__ = "family"
    id = Column(Integer, prymary_key = True)
    #fk
    emergence_contact_id = Column(Integer)
    
class FamilyChildren(Base):
    __tablename__ = "family-children"
    #fk
    child_id = Column(Integer)
    #fk
    family_id = Column(Integer)
    
class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, prymary_key = True)
    name = Column(String)
    bith_date = Column(Date)
    gender = Column(String)
    spectrum_degree = Column(String)
    #family_id = Column(Integer)
    #fk
    trait_id = Column(String)
class Traits(Base):
    __tablename__ = "traits"
    id = Column(Integer, prymary_key=True)
    isvalid = Column(Boolean)
    value = Column(String)
    #fk
    child_id = Column(Integer)
    #fk
    tag_id = Column(Integer)
class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, prymary_key=True)
    value = Column(String)
class SchoolAdministrators(Base):
    __tablename__ = "school-administrators"
    id = Column(Integer, prymary_key = True)
    #foreign
    admin_user_id  = Column(Integer)
    #foreign
    school_id = Column(Integer)

class Schools(Base):
    __tablename__ = "schools"
    id = Column(Integer, prymary_key = True )
    name = Column(String)
    address = Column(String)
    contact_email = Column(String)
    contact_telephone = Column(String)

#isso vem de usuario ou nao tem relacionamento
class SchoolProfessionals(Base):
    __tablename__ = "schools-professionals"
    id = Column(Integer, prymary_key = True )
    name = Column(String)
    email = Column(String)
    role = Column(String)
    cpf = Column(String)
    address = Column(String)
    #fk
    school_id = Column(Integer)


class SchoolProfessionalAssignments(Base):
    __tablename__ = "School-Professional-assignments"
    #fk
    professional_id = Column(Integer)
    employment_date = Column(Date)
    #fk
    school_id = Column(Integer)
    
#aberto a discussoes    
class DevelopmentDiaries(Base):
    __tablename__ = "Development-diaries"
    id = Column(Integer, prymary_key= True)
    #fk
    child_id = Column(Integer)
    entry_date = Column(Date)
    entry_text = Column(Text)
    tittle = Column(String)
    detail_treat = Column(JSON)
    #fk
    assigned_professional_id = Column(Integer)
    entry_category_tag = Column(String)
    
class SchoolStudents(Base):
    __tablename__ = "School-students"
    #fk
    child_id = Column(Integer)
    admission_date = Column(Date)
    #fk
    school_id = Column(Integer)
    
class DevelopmentDiaryChildDetails(Base):
    __tablename__ = "Development-diary-child-details"
    #fk
    child_id = Column(Integer)
    #fk
    trait_id = Column(Integer)
    #fk
    development_diary_id = Column(Integer)