from pydantic import BaseModel
from typing import List
from child import Child
    
class Family(BaseModel):
    family_id: int
    children: List[Child]    
    
