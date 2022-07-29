from fastapi import status, HTTPException, Response, APIRouter, Depends
from .. import schemas, Oathou2

from typing import List, Optional
from .dtbase import database


router= APIRouter()


conn= database.connection()
cur = conn.cursor()

@router.get("/")
def fist_page():
    return {"message": "welcome to my application hamza"}

@router.get("/posts", response_model=List[schemas.All_details])
def get_all_posts(current_user=Depends(Oathou2.get_current_user), limit: int = 20, search: str ="" ):
    user_id = current_user.id
    searching= "%"+search+"%"
    cur.execute(""" select p.name as "post_name",
       p.content ,
       p.id as "post_id",
       p.user_id as "user_id",
       
       u.name as "user_name",
       u.email  , 
       u.id as "id_user"
     from page p join user_account u
      on p.user_id = u.id 
     where user_id=(%s) and p.content like %s limit (%s) """,
                (user_id, searching, limit))
    posts = cur.fetchall()
    return posts

@router.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post_response)
def create_posts(post: schemas.Post_create, current_user = Depends(Oathou2.get_current_user)):
    user_id= current_user.id
#TODO extract the user name from the object current_user
    cur.execute("""INSERT INTO page(name, content , published, user_id ) values(%s ,%s , %s, %s) returning * """,
                (post.name, post.content, post.published, user_id))
    post=cur.fetchone()
    conn.commit()
    return post
@router.get("/posts/{id}", response_model=schemas.Post_response)
def get_post(id: int):
    cur.execute("""Select * from page where id= %s """, (str(id),))
    post=cur.fetchone()
    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"the id {id} is not found")
    return post
@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def del_post(id: int, current_user=Depends(Oathou2.get_current_user)):
    user_id=current_user.id
    cur.execute("""select user_id from page where id = %s""", (str(id),))
    post_owner=cur.fetchone()
    if post_owner is None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="the post with the id : {id} doesn't exist")
    if int(user_id) != int(post_owner["user_id"]):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="you are not the owner of"
                                                                          "this  post")
    else:
        cur.execute("""delete from page where id = %s""", (str(id),))
        conn.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/posts/{id}", response_model= schemas.Post_response)
def update_post(id : int, post : schemas.Post_create, current_user = Depends(Oathou2.get_current_user)):
    user_id = current_user.id
    cur.execute("""select user_id from page where id = %s""", (str(id),))
    post_owner = cur.fetchone()
    if int(user_id) != int(post_owner["user_id"]):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="you are not the owner of"
                                                                          "this  post")

    cur.execute("""update page set name=%s , content=%s where id=%s RETURNING *  """,
                (post.name, post.content, str(id)))
    new_post=cur.fetchone()
    conn.commit()

    return new_post
