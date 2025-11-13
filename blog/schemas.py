from pydantic import BaseModel


# Blog schema
class Blog(BaseModel):
    title : str
    body : str

class ShowBlog(Blog):
    title : str
    class Config():
        orm_mode = True
