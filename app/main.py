
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





app.include_router(posts.router)
app.include_router(users.router)
app.include_router(authen.router)
app.include_router(vote.router)