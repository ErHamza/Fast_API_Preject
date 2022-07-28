from fastapi import APIRouter, Depends, Response
from .. import schemas
from .dtbase import database
from fastapi import HTTPException, status
from .. import utility, Oathou2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

conn= database.connection()
cur= conn.cursor()
router=APIRouter()

@router.post("/login", response_model= schemas.Token)

def login(data: OAuth2PasswordRequestForm = Depends() ):
    cur.execute("""Select * from user_account where email = %s""", (data.username,))
    user= cur.fetchone()

    if not user:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="something wrong")
    if utility.verify(data.password, user["password"]):
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="something wrong")
    token= Oathou2.create_access_token({"id": user["id"], "name": user["name"]})
    return {"access_token": token, "token_type": "Bearer"}

