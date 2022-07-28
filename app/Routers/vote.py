from fastapi import APIRouter, status, Response, Depends, HTTPException
from .dtbase import  database
from .. import schemas, Oathou2



conn = database.connection()
cur = conn.cursor()
router = APIRouter()
@router.post("/vote", status_code=status.HTTP_201_CREATED)
def vote(vote : schemas.Vote, current_user= Depends(Oathou2.get_current_user)):
    cur.execute("""select * from vote where user_id = (%s) and post_id=(%s)  """, (current_user.id , vote.post_id,))
    result= cur.fetchall()
    if vote.dir ==1:
        if result:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"you have"
                                                                             f" already liked the post{vote.post_id}")
        cur.execute("""insert into vote(user_id, post_id) values(%s, %s)""", (current_user.id, vote.post_id,))
        conn.commit()
        return {"message": "you have voted"}
    else :
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="you haven't voted yet")
        cur.execute("""delete from vote where user_id =(%s) and post_id= (%s)""", (current_user.id, vote.post_id,))
        conn.commit()
        return {"message": "you have deleted the vote"}


@router.get("/vote/{id}")
def votes(id :int):
    cur.execute("""Select p.name as "post_name", count(v.*) as "likes"
     from vote v right join page p on v.post_id = p.id
     group by name , p.id
      having p.id =(%s)""", (str(id),))
    result=cur.fetchone()
    return {"likes": result["likes"]}

