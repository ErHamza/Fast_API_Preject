
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .Routers import posts, users, authen, vote
app = FastAPI()

origins=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




#my_posts=[{"title":"la vie a l'ensem","content":"amazing life" ,"id":1}]
#def find_post(id):
  #  for p in my_posts:
#        if p['id']==id:
 #           return p


#def find_index(id):
   # for index , p in enumerate(my_posts):
  #      if id==p['id']:
 #           return index
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(authen.router)
app.include_router(vote.router)