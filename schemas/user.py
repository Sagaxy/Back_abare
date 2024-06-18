from sqlalchemy import create_engine, Column, Integer, String, Date, 
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
    #foreingkey
    emergence_contact_id = Column(Integer)
    
class FamilyChildren(Base):
    __tablename__ = "family-children"
    #foreingkey
    child_id = Column(Integer)
    #foreingkey
    family_id = Column(Integer)
    
class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, prymary_key = True)
    name = Column(String)
    bith_date = Column(Date)
    gender = Column(String)
    spectrum_degree = Column(String)
    #family_id = Column(Integer)
    #foreign
    trait_id = Column(String)

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, prymary_key=True)
    value = Column(String)
    #foreign
    tag_kind_id = Column(Integer, )
    
class TagKind(Base):
    __tablename__ = "tag-kind"
    id = Column(Integer, prymary_key = True)
    kind = Column(String)

class Traits(Base):
    __tablename__ = "traits"
    id = Column(Integer, prymary_key=True)
    value = Column(String)

class TraitsTags(Base):
    __tablename__ = "traits-tags"
    #foreign
    trait_id = Column(Integer)
    #foreign
    tag_id = Column(Integer)

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
class schoolProfessionals(Base):
    __tablename__ = "schools-professionals"
    id = Column(Integer, prymary_key = True )
    name = Column(String)
    email = Column(String)
    role = Column(String)
    cpf = Column(String)
    address = Column(String)
    #fk
    school_id = Column(Integer)
