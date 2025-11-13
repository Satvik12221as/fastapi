from pydantic import BaseModel

# Blog schema
class Blog(BaseModel):
    title : str
    body : str


# Show Blog schema with title only
class ShowBlog(BaseModel):
    title : str
    body : str
    class Config():
        orm_mode = True


# User schema
class user(BaseModel):
    name : str
    email : str
    password : str
