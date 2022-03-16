from fastapi import APIRouter, Depends
from .. import schemas, database, oauth2
from typing import List
from sqlalchemy.orm import Session
from ..repository import post

router = APIRouter(prefix="/post", tags=["Posting"])
get_db = database.get_db


@router.get("/", response_model=List[schemas.ShowPost])
def all(
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return post.get_all(db)


@router.post("/")
def create(
    request: schemas.Post,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return post.create(request, db)


@router.delete("/{id}")
def erase(
    id,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return post.destroy(id, db)


@router.put("/{id}")
def update(
    id,
    request: schemas.Post,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return post.update(id, request, db)


@router.get("/{id}")
def show(
    id,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return post.show(id, db)
