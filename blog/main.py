from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to my demo-api"}

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)