from sqlalchemy import select
from sqlalchemy.orm import Session,joinedload
from .. import models, schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    post = db.query(models.Post).all()
    return post

def get_all_tab(db:Session):
    stmt = select(models.Post).options(joinedload(models.Post.comments),joinedload(models.Post.comments,models.Comment.creator))
    result = db.execute(stmt).scalars().unique()
    # result = db.query(models.Post).all()
    return result

def create(request: schemas.Post,user_id:int, db: Session):
    new_post = models.Post(
        title=request.title, text=request.text,user_id=user_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def destroy(id: int, db: Session):
    post = db.query(models.Post).filter(models.Post.id == id)
    comment = db.query(models.Comment).filter(models.Comment.post_id == id)
    if not post.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found"
        )
    comment.delete(synchronize_session=False)
    post.delete(synchronize_session=False)
    db.commit()
    return HTTPException(status_code=status.HTTP_202_ACCEPTED,detail=f"post with id {id} was deleted ",headers=[])


def update(id: int, request: schemas.Post, db: Session):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id{id} not found"
        )
    
    post.update({"title": request.title, "text" :request.text})
    db.commit()
    
    return HTTPException(status_code=status.HTTP_202_ACCEPTED,detail=f"post with id {id} was updated with title:{request.title} and text:{request.text}",headers=[])
    


def show(id: int, db: Session):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with the id {id} is not available",
        )
    return post
