from asyncio.windows_events import NULL
from fastapi import APIRouter, Depends
from .. import schemas, database, oauth2
from typing import List
from sqlalchemy.orm import Session
from ..repository import post

router = APIRouter(prefix="/post", tags=["Posting"])
get_db = database.get_db


@router.get("/", response_model=List[schemas.ShowPost])
def all_post(
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return post.get_all(db)

@router.get("/alltab",response_model=NULL)
def alltab(
    db:Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),):
    return post.get_all_tab(db)

@router.post("/")
def create_post(
    request: schemas.Post,
    db: Session = Depends(get_db),
    current_user: schemas.TokenData = Depends(oauth2.get_current_user),
):
    return vars(post.create(request,current_user.id, db))


@router.delete("/{id}")
def erase_post(
    id,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return post.destroy(id, db)


@router.put("/{id}")
def update_post(
    id,
    request: schemas.Post,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return post.update(id, request, db)


@router.get("/{id}")
def show_post(
    id,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return post.show(id, db)
