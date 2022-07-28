from .database import base
from sqlalchemy import Integer, column, String, Boolean
from sqlalchemy.sql.expression import null




class Post(base):
    __tablename__= "posts"
    id = column(Integer, primary_key=True, nullable=False)
    title= column(String , nullable= False)
    content= column(String , nullable=False)
    published = column(Boolean , default = True )
