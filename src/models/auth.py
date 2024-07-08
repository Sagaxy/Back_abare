from pydantic import BaseModel


class LoginRequest(BaseModel):
    email: str
    password: str

class Authentication(BaseModel):
    access_type: int
    user_id: int