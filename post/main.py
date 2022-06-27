import asyncio

from fastapi import FastAPI
from sqlalchemy.exc import OperationalError

from . import models
from .database import engine
from .router import post, user, comment, authentication

app = FastAPI()

app.include_router(authentication.router)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(comment.router)


@app.on_event("startup")
async def startup():
    success = False
    while not success:
        try:
            models.Base.metadata.create_all(engine)
        except OperationalError:
            await asyncio.sleep(5.0)
        else:
            success = True
