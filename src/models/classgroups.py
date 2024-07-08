from pydantic import BaseModel
from typing import List

from models.children import ChildAbbreviated


class ClassGroupWithChildren(BaseModel):
    id: int
    name: str
    childrenAmount: int
    children: List[ChildAbbreviated]

    def __init__(self, data_dict: dict, children: List[ChildAbbreviated]):
        self.id = data_dict["id"]
        self.name = data_dict["name"]
        self.childrenAmount = len(children)
        self.children = children

class ClassGroupsWithChildren(BaseModel):
    classgroups: List[ClassGroupWithChildren]