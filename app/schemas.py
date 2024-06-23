from pydantic import BaseModel
from typing import Optional
from enum import Enum



class UserLevel(Enum):
    beginner = 'beginner'
    intermediate = 'intermediate',
    expert = 'expert'


class UserBase(BaseModel):
    id: int
    email:str
    username:str
    password: str
    age: Optional[int] = None
    level: UserLevel = UserLevel.beginner

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    username: Optional[str] = None
    access_token: str
    token_type: str

