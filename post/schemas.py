from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    password: str


class Post(BaseModel): 
    id:int
    title: str
    text: str
    
class Comment(BaseModel):
    post_id:int
    text: str


class ShowUser(BaseModel):
    username: str
    email: str
    


class ShowComment(BaseModel):
    text: str
    post_id : int

    class Config:
        orm_mode = True

class UserPost(BaseModel):
    user_id : int
    username: str
    
class ShowPost(BaseModel):
    title:str
    text: str
    user_id:int

    class Config:
        orm_mode = True
    
    
class Login(BaseModel):
    email : str
    password : str
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id : Optional[int] = None
