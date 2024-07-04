from typing_extensions import Unpack
from pydantic import BaseModel, ConfigDict
from typing import List, Dict
import datetime
import dateutil.parser as dparser

class Child(BaseModel):
    child_id: int
    picture: str
    name: str
    age: int
    gender: str
    
    def __init__(self,id: int, name: str, age: str, gender: str, picture: str|None = None):
        self.child_id = id
        self.picture = picture if picture else ""
        self.name = name
        datetime_age = dparser.parse(age)
        current_date = datetime.datetime.today()
        self.age = current_date.year - datetime_age.year - ((current_date.month, current_date.day) < (datetime_age.month, datetime_age.day))
        self.gender = "Masculino" if gender == "M" or gender == "m" else "Feminino"
        
        
class Tag(BaseModel):
    value: str

class ChildDetails(Child):
    spectrum_degree: str
    traits: Dict[str,List[Tag]]
    
class DiaryRecord(BaseModel):
    diary_id: int
    title: str
    entry_date: str | None = None
    entry_parent_text: str | None
    entry_school_text: str | None
    professional_name: str | None
    related_tag: List[Tag] | None = None
    
    def __init__(self, id: int, tittle: str,  entry_parent_text: str | None = None, entry_school_text: str | None = None, professional_name: str | None = None, related_tag: List[Tag] | None = None ):
        self.diary_id = id
        self.title = tittle
        self.entry_date = self.entry_date if self.entry_date else datetime.datetime.today()
        self.entry_parent_text = entry_parent_text
        self.entry_school_text = entry_school_text
        self.professional_name = professional_name
        self.related_tag = related_tag
    
    
class DiaryRecords(BaseModel):
    records: List[DiaryRecord]
