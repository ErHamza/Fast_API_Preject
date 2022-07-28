from jose import JWSError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from . import schemas
from .Config import settings

Oauth_scheme = OAuth2PasswordBearer(tokenUrl='login')



secret_ky=settings.secret_key
ALGORITHM = settings.algorithme
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_time
#TODO the error message after the experation of the access token
def create_access_token(data : dict):
    var= data.copy()
    expire_token= datetime.utcnow()+ timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    var.update({"exp": expire_token })
    token = jwt.encode(var, secret_ky , algorithm=ALGORITHM)
    return token
def verify_access_token(token: str , credentials_exception):
    try:
            payload = jwt.decode(token, secret_ky, algorithms=[ALGORITHM])
            id: str = payload.get("id")
            if id is None:
                raise credentials_exception
            token_data = schemas.Tokendata(id=id)

    except JWSError:
        raise credentials_exception
    return token_data

def get_current_user(token :str = Depends(Oauth_scheme)):
    credentials_exceptions = HTTPException(status.HTTP_401_UNAUTHORIZED, detail="you are not welcome")
    return verify_access_token(token, credentials_exceptions)
