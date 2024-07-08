from pydantic import BaseModel
from typing import List


class UserAbbreviated(BaseModel):
    id: int
    name: str
    access_type: int

    def __init__(self, data_dict: dict) -> None:
        self.id = data_dict["id"]
        self.name = data_dict["name"]
        self.access_type = data_dict["access_type"]

class UsersAbbreviated(BaseModel):
    users: List[UserAbbreviated]

class UserDetails(BaseModel):
    id: int
    name: str
    cpf: str
    phone: str

    def __init__(self, data_dict: dict) -> None:
        self.id = data_dict["id"]
        self.name = data_dict["name"]
        self.cpf = data_dict["cpf"]
        self.phone = data_dict["phone"]