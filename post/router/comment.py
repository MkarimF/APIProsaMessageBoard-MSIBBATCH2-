from fastapi import APIRouter, Depends
from fastapi import APIRouter
from .. import database, schemas, oauth2
from sqlalchemy.orm import Session
from ..repository import comment
from typing import List

router = APIRouter(prefix="/comment", tags=["Comment"])
get_db = database.get_db


@router.post("/", response_model=schemas.ShowComment)
def create_comment(
    request: schemas.Comment,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return comment.create(request,current_user.id, db)


@router.get("/{id}", response_model=schemas.ShowComment)
def get_comment(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.Comment = Depends(oauth2.get_current_user),
):
    return comment.show(id, db)


@router.get("/", response_model=List[schemas.ShowComment])
def all(db: Session = Depends(get_db)):
    return comment.get_all(db)
