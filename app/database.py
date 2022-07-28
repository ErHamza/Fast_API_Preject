from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
sql_alchemy_url='postgresql://postgres:ing@localhost/fastAPI'
engine= create_engine(sql_alchemy_url)
session_local= sessionmaker(autocommit= False , autoflush= False , bind=engine)
base = declarative_base()
