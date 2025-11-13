from .database import Base
from sqlalchemy import Column, Integer, String, Boolean

# Create Blog model
class Blog(Base):



# table name and columns
    __tablename__ = 'blogs'
    id = Column(Integer , primary_key=True , index=True)
    title = Column(String)
    body = Column(String)


# Create User table model
class user(Base):
    __tablename__ = 'users'
    id = Column(Integer , primary_key=True , index=True)
    name = Column(String)
    email = Column(String , unique=True , index=True)
    password = Column(String)




