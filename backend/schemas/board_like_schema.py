from pydantic import BaseModel
from datetime import datetime

class BoardLikeInfo(BaseModel):
    user_id: int
    board_id: int

    class Config:
        orm_mode = True
