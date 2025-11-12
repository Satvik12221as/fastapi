from .database import Base
from sqlalchemy import Column, Integer, String, Boolean

# Create Blog model
class Blog(Base):

# table name and columns
    __tablename__ = 'blogs'
    id = Column(Integer , primary_key=True , index=True)
    title = Column(String)
    body = Column(String)


