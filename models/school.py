from pydantic import BaseModel
from typing import List
from child import Child

    
class ClassGroup(BaseModel):
    class_group_id: int
    name: str
    qnt_students: int
    students: List[Child]
    