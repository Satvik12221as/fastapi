from pydantic import BaseModel


# blog schema
class Blog(BaseModel):
    title : str
    body : str