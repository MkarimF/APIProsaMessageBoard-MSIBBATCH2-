from fastapi import FastAPI
from . import models
from .database import engine
from .router import post, user, comment

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(comment.router)
