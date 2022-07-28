from .. import utility
from fastapi import responses, status, HTTPException, APIRouter
from .. import schemas
from .dtbase import database
from psycopg2.extras import RealDictCursor
from typing import List


router= APIRouter(
    prefix="/users"
)


conn= database.connection()
cur = conn.cursor()


@router.get("/", response_model= List[schemas.show_users])
def show_users():
    cur.execute("""select * from user_account""")
    u=cur.fetchall()
    conn.commit()
    return u


@router.post("/adduser", response_model=schemas.Created_account)
def add_user(send: schemas.User_model):
    pa= send.password
    password=utility.hash(pa)



    cur.execute("""INSERT INTO user_account(name, email , password ) 
    values(%s ,%s , %s) returning * """, (send.name, send.email, password,))
    new_user= cur.fetchone()
    conn.commit()
    return new_user
#TODO fix : the server stops when the user enter same email for two users