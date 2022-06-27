import os
from typing import List
from starlette.responses import Response
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import database, schemas, oauth2
from ..repository import user

router = APIRouter(prefix="/user", tags=["User"])
get_db = database.get_db


@router.get("/", response_model=List[schemas.ShowUser])
def all_user(
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(oauth2.get_current_user),
) -> schemas.ShowUser:
    return user.get_all(db)


@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)) -> schemas.ShowUser:
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
