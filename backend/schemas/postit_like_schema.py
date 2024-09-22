from pydantic import BaseModel
from datetime import datetime

class PostItLikeInfo(BaseModel):
    user_id:int
    postit_id:int

    class Config:
        orm_mode = True

