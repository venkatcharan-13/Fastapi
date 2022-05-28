from .importss import *

class Post(BaseModel):
    user_id:int
    post_id:int
    title:str
    body:str

class Geo(BaseModel):
    lat: str
    lnl: str

class Address(BaseModel):
    street:str
    suite:str
    city:str
    zipcode:str
    geo:Geo

class Company(BaseModel):
    name: str
    catchphrase:str
    bs: str

class User(BaseModel):
    user_id:int
    name:str
    username:str
    email:str
    phone:str
    website:str
    phone : str
    website: str
    company: Company
    address: Address

class Comments(BaseModel):
    post_id:int
    comments_id:int
    name:str
    email:str
    body:str

