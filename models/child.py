from pydantic import BaseModel
from typing import List, Dict


class Child(BaseModel):
    child_id: int
    picture: str
    name: str
    age: int
    gender: str
    
class Tag(BaseModel):
    value: str

class ChildDetails(Child):
    spectrum_degree: str
    traits: Dict[str,List[Tag]]
    
class DiaryRecord(BaseModel):
    diary_id: int
    title: str
    entry_date: str
    entry_parent_text: str | None
    entry_school_text: str | None
    professional_name: str | None
    related_tag: List[Tag] | None = None
    
class DiaryRecords(BaseModel):
    records: List[DiaryRecord]
