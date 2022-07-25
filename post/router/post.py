from unittest import result
from fastapi import APIRouter, Depends, Path
from .. import schemas, database, oauth2, models
from typing import List
from sqlalchemy.orm import Session
from ..repository import post

router = APIRouter(prefix="/post", tags=["Posting"])
get_db = database.get_db


def orm_to_comment(comment: models.Comment) -> schemas.ShowComment:
    return schemas.ShowComment(id=comment.id, text=comment.text, post_id=comment.post_id,
                               creator=schemas.ShowUser(username=comment.creator.username, email=comment.creator.email))


def orm_to_post(post: models.Post) -> schemas.ShowPost:
    return schemas.ShowPost(title=post.title, text=post.text, user_id=post.user_id, id=post.id,
                            comments=[orm_to_comment(comment) for comment in post.comments])


@router.get("/all_tab", response_model=List[schemas.ShowPost])
def all_post(
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(oauth2.get_current_user)) -> schemas.ShowPost:
    result = post.get_all_tab(db)
    # return list(result)

    return [orm_to_post(item) for item in result]


@router.get("/{id}")
def show_post(
        id,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(oauth2.get_current_user),
) -> schemas.ShowPost:
    return post.show(id, db)


@router.post("/")
def create_post(
        request: schemas.Post,
        db: Session = Depends(get_db),
        current_user: schemas.TokenData = Depends(oauth2.get_current_user),
) -> schemas.Post:
    return vars(post.create(request, current_user.id, db))


@router.delete("/{id}", )
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
) -> schemas.Post:
    return post.update(id, request, db)

# @router.get("/{id}/comments")
# def get_all_comments_of_a_post(post_id:int = Path(...,alias="id"))->List[schemas.ShowComment]:
#     raise NotImplementedError()