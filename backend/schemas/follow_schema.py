from pydantic import BaseModel
from datetime import datetime

class FollowBase(BaseModel):
    class Config:
        orm_mode = True

class FollowerInfo(FollowBase):
    follower_id:int

class FollowingInfo(FollowBase):
    followed_id:int

class FollowInfo(FollowBase):
    followed_id:int
    created_at:datetime
    follower_id:int

