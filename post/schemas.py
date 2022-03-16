from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    password: str


class Post(BaseModel): 
    judul: str
    isi: str
    kategori: str


class Comment(BaseModel):
    isi: str


class ShowUser(BaseModel):
    username: str
    email: str
    posts: List[Post] = []

    class Config:
        orm_mode = True


class ShowComment(BaseModel):
    isi: str
    Commentator: List[Comment] = []

    class Config:
        orm_mode = True


class ShowPost(BaseModel):
    kategori: str
    isi: str
    creator: ShowUser
    comment: ShowComment
    
class Login(BaseModel):
    username : str
    password : str
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
