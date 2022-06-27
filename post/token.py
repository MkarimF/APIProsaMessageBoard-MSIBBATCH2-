from datetime import datetime, timedelta

from jose import JWTError, jwt

from . import schemas, creds

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, creds.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, creds.SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("username")
        email: str = payload.get("email")
        id: int = payload.get("id")
        if id is None:
            raise credentials_exception
        print(payload)
        token_data = schemas.TokenData(id=id, email=email, username=username)

    except JWTError:
        raise credentials_exception
    return token_data
