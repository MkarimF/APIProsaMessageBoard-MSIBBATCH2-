from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from . import token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/oauth2/")
oauth2_scheme2 = OAuth2PasswordBearer(tokenUrl="/login/")


def get_current_user(data: str = Depends(oauth2_scheme2)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token.verify_token(data, credentials_exception)


def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token.verify_token(data, credentials_exception)

# class HTTPBearer(get_current_user):
#     def __init__(
#         self,
# *,
#         bearerFormat: Optional[str] = None,
#         scheme_name: Optional[str] = None,
#         description: Optional[str] = None,
#         auto_error: bool = True,
#     ):
#         self.model = HTTPBearerModel(bearerFormat=bearerFormat, description=description)
#         self.scheme_name = scheme_name or self.__class__.__name__
#         self.auto_error = auto_error

#     async def __call__(
#         self, request: Request
#     ) -> Optional[HTTPAuthorizationCredentials]:
#         authorization: str = request.headers.get("Authorization")
#         scheme, credentials = get_authorization_scheme_param(authorization)
#         if not (authorization and scheme and credentials):
#             if self.auto_error:
#                 raise HTTPException(
#                     status_code=HTTP_403_FORBIDDEN, detail="Not authenticated"
#                 )
#             else:
#                 return None
#         if scheme.lower() != "bearer":
#             if self.auto_error:
#                 raise HTTPException(
#                     status_code=HTTP_403_FORBIDDEN,
#                     detail="Invalid authentication credentials",
#                 )
#             else:
#                 return None
#         return HTTPAuthorizationCredentials(scheme=scheme, credentials=credentials)
