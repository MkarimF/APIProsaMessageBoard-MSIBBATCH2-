from turtle import title
from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    post = db.query(models.Post).all()
    return post


def create(request: schemas.Post, db: Session):
    new_post = models.Post(
        title=request.title, body=request.body, user_id=request.user_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def destroy(id: int, db: Session):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found"
        )

    post.delete(synchronize_session=False)
    db.commit()
    return "done"


def update(id: int, request: schemas.Post, db: Session):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id{id} not found"
        )

    post.update({"text": request.text, "kategori": request.kategori})
    db.commit()
    return "updated"


def show(id: int, db: Session):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with the id {id} is not available",
        )
    return post
