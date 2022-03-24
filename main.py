from fastapi import FastAPI
from . import models
from .post.database import engine
from .post.router import post, user, comment, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(comment.router)