from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"data" : 'blog list'} 

@app.get("/blog/unpublished")
def unpublished():
    return {"data" : 'all unpublished blogs'}

# fetch blog by id
@app.get("/blog/{id}")
def about(id : int):
    return {"data" : id}

# fetch comments of a blog by id
@app.get("/blog/{id}/comments")
def comments(id):
    return {"data" : {'1', '2'}}

@app.get("/blog/{id}/references")
def references(id):
    return {"data" : {'sexy', 'hot'}}