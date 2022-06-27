from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from requests import request
from .. import schemas, database, models, token
from ..hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(
    tags=['Authentication']
)


@router.post('/login/oauth2')
def login_oauth(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"invalid Credentials")

    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"incorrect password")
    # generating a jwt token  return it
    access_token = token.create_access_token(data={"id": user.id,
                                                   "email": user.email,
                                                   "username": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"invalid Credentials")

    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"incorrect password")
    # generating a jwt token  return it
    access_token = token.create_access_token(data={"id": user.id,
                                                   "email": user.email,
                                                   "username": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
