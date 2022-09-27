from typing import List, Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    hashed_password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class GguBase(BaseModel):
    reg: str
    
class Ggu(GguBase):
    id: int
    
    class Config:
        orm_mode = True
        
class SecretBase(BaseModel):
    skey: str
    
class Secret(SecretBase):
    id: int
    
    class Config:
        orm_mode = True
        
class RegistBase(BaseModel):
    regkey: str
    
class Regist(RegistBase):
    id: int
    
    class Config:
        orm_mode = True