from pydantic import BaseModel


# Blog schema
class Blog(BaseModel):
    title : str
    body : str