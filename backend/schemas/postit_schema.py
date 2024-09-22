from pydantic import BaseModel
from datetime import datetime


class PostitBase(BaseModel):
    class Config:
        orm_mode = True

class PostitCreate(PostitBase):
    address:str
    content:str

class PostitInfo(PostitBase):
    address:str
    like:int
    postit_id:int
    user_id:int
    content:str


class PostItDetail(PostitBase):
    address:str
    like:int
    created_at:datetime
    updated_at:datetime
    content:str
    user_id:int
    
