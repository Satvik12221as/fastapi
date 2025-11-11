from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/blog")
def index(limit=10, published: Optional[bool]=True , sort: Optional[str]=None):
    if published:
        return {"data" : f'{limit} published blogs'} 
    else:
        return {"data" : f'{limit} all blogs'}

@app.get("/blog/unpublished")
def unpublished():
    return {"data" : 'all unpublished blogs'}

# Fetch blog by id
@app.get("/blog/{id}")
def about(id : int):
    return {"data" : id}

# Fetch comments of a blog by id
@app.get("/blog/{id}/comments")
def comments(id , limit=10):
    return limit
    return {"data" : {'1', '2'}}

class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool]

# Post created
@app.post('/blog')
def create_blog(blog : Blog):
    return {"data" : f'blog is created as {blog.title}'}