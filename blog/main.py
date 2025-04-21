from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from . import models
from .database import engine
from .routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

html_content = """
<html>
    <head>
        <title>FastAPI Demo</title>
        
    </head>
    <body>
        <h1>Welcome to My FastAPI Demo API 🚀</h1>
        <p>Click below to view the interactive API docs:</p>
        <a href="/docs" target="_blank" style="font-size: 25px; color: #2196F3; font-weight: bold;">Go to Swagger Docs</a>
    </body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def read_root():
    return html_content

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)