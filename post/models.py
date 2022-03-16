
from sqlalchemy import Column, ForeignKey, Integer, String
from .database import Base
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    creator = relationship("User")


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    
class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    category = Column(String)
    creator_id = Column(Integer, ForeignKey(User.id))
    creator = relationship("User")
    post_id = Column(Integer, ForeignKey(Post.id))
    post = relationship("Post")
