import email
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
    id : int
    
    class Config:
        orm_mode = True
        

class showAll(BaseModel):
    title:str
    text: str
    user_id:int
    id : int
    username:str
    email:str
    comment_id:int
    
    
    
# [
#   {
#     "title": "string",
#     "text": "string",
#     "user_id": 0,
#     "id": 0,
#     "creator": {
#       "username": "string",
#       "email": "string"
#     },
#     "Comments": [
#         {
#         "title": "string",
#         "text": "string",
#         "user_id": 0,
#         "id": 0,
#         "creator": {
#           "username": "string",
#           "email": "string"
#         },
#       }
#     ]
#   }
# ]    
    
class Login(BaseModel):
    email : str
    password : str
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id : Optional[int] = None
