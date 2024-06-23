from sqlalchemy import Column, Integer, String
from sqlalchemy import Enum as EnumColumn

from app.db import Base
from app.schemas import UserLevel


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    age = Column(Integer)
    level = Column(EnumColumn(UserLevel))
