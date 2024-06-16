from pydantic import BaseModel


class Login(BaseModel):
    email: str
    password: str

class Auth(BaseModel):
    access: int
    user_id: int
