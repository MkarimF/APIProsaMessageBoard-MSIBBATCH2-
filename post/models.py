from sqlalchemy import Column, ForeignKey, Integer, String
from sqlmodel import Relationship
from .database import Base
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    text = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    creator = relationship("User")
    # commentator = Column(Integer, ForeignKey("comments.post_id"))
    # creator_comment = relationship("Comment")

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
    creator_id = Column(Integer, ForeignKey(User.id))
    creator = relationship("User")
    post_id = Column(Integer, ForeignKey(Post.id))
    post = relationship("Post")
