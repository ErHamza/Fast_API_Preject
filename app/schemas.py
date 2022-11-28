from pydantic import BaseModel , EmailStr, conint
from datetime import datetime,date, time
from typing import Optional
class Post_base(BaseModel):
       name: str
       content: str
       published: bool= True

class Post_create(Post_base):
       pass

class show_users(BaseModel):
       name:str
       email: str
       id : int

class Post_response(BaseModel):
       name:str
       content:str
       id :int
       user_id : int

#todo add created_att

class User_model(BaseModel):
       name:str
       email: EmailStr
       password: str

class Created_account(BaseModel):
       name:str
       email:str



class Authentification(BaseModel):
       email : EmailStr
       password: str


class Tokendata(BaseModel):
       id: Optional[str]=None
       name: Optional[str] = None
class Token(BaseModel):
       access_token: str
       token_type:str
       name:str
       expire_time:str
       email:str

class All_details(BaseModel):
       post_name: str
       content: str
       post_id: int
       user_id: int
       user_name:str
       email: str
       id_user: int
       created_at : datetime


# In Herolu DB the column created_at is not created


class Vote(BaseModel):
       post_id : int
       dir : conint(le=1)
class votes(BaseModel):
       post_id: int