from .importss import *

class User(Base):
    __tablename__="users"
    user_id = Column(Integer, primary_key= True, index=True, unique=True)
    name = Column(String)
    username = Column(String)
    email = Column(String)
    address=Column(JSON())
    phone = Column(String)
    website = Column(String)
    company=Column(JSON())
    

class Post(Base):
    __tablename__ ="posts"
    user_id= Column(Integer,unique=False,nullable=False)
    post_id=Column(Integer,unique=True,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    body= Column(String,nullable=False)

class Comments(Base):
    __tablename__="comments"
    post_id=Column(Integer,unique=False)
    comments_id=Column(Integer,primary_key=True,index=True,unique=True)
    name=Column(String)
    email=Column(String)
    body=Column(String)

