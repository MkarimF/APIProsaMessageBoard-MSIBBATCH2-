import os
from uuid import uuid4

import mimetypes

from starlette.responses import Response
from fastapi import APIRouter, Depends, UploadFile,Form
from sqlalchemy.orm import Session

from .. import database, schemas
from ..repository import user

router = APIRouter(prefix="/user", tags=["User"])
get_db = database.get_db

MEDIA_ROOT = "media"
IMAGE_ROOT = os.path.join(MEDIA_ROOT, "/images")


@router.post("/", response_model=schemas.ShowUser)
def create_user(request:schemas.User,  db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)


# @router.get("/{id}/profile_picture", responses={
#     "200": {
#         "content": {
#             "images/jpeg": {}
#         }
#     }
# })
# def get_user_profile_picture(id: int, db: Session = Depends(get_db)):
#     _user = user.show(id, db)

#     with open(_user.profile_picture_path, "rb") as f:
#         mimetype, _ = mimetypes.guess_type(_user.profile_picture_path)
#         return Response(content=f.read(), media_type=mimetype)
