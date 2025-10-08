from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"name": "Satvik", "age": 21}

@app.get("/about")
def about():
    return {"about": "I am a software developer."}