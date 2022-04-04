from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    password: str


class Post(BaseModel): 
    title: str
    text: str
    
class Comment(BaseModel):
    post_id:int
    text: str


class ShowUser(BaseModel):
    username: str
    email: str
    post: List[Post] = []

    class Config:
        orm_mode = True


class ShowComment(BaseModel):
    text: str
    Commentator: List[Comment] = []

    class Config:
        orm_mode = True


class ShowPost(BaseModel):
    title:str
    text: str
    Creator: List[User] = []

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
