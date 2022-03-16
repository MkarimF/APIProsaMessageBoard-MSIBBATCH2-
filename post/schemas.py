from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    id:int
    username: str
    email: str
    password: str


class Post(BaseModel): 
    title: str
    text: str
    
class Comment(BaseModel):
    isi: str


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
    text: str
    creator: ShowUser
    comment: ShowComment
    
class Login(BaseModel):
    email : str
    password : str
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id : Optional[int] = None
