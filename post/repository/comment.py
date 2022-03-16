from cgitb import text
from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status


def create(request: schemas.Comment,creator_id:int, db: Session):
    new_comment = models.Comment(
        text=request.text, kategori=request.kategori, creator_id=request.creator_id
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def show(id: int, db: Session):
    comment = db.query(models.Comment).filter(models.Comment.id == id).first()
    if not comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the id {id} is not available",
        )

    return comment
