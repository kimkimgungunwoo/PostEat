from pydantic import BaseModel
from datetime import datetime

    
class starInfo(BaseModel):
    board_id:int
    created_at:datetime

    class Config:
        orm_mode = True

