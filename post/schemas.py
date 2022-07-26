from typing import List, Optional

from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    password: str


class Post(BaseModel):
    title: str
    text: str

    class Config:
        orm_mode = True


class Comment(BaseModel):
    post_id: int
    text: str


class ShowUser(BaseModel):
    id:int
    username: str
    email: str

    class Config:
        orm_mode = True


class ShowComment(BaseModel):
    post : Post
    id: int
    text: str
    post_id: int
    creator: ShowUser

    class Config:
        orm_mode = True


class ShowPost(BaseModel):
    title: str
    text: str
    user_id: int
    id: int
    comments: List[ShowComment] = []

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None
