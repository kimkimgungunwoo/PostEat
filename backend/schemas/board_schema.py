from pydantic import BaseModel

class BoardBase(BaseModel):
    board_name:str
    class Config:
        orm_mode = True

class BoardCreate(BoardBase):
    pass

class BoardCreateResponse(BoardBase):
    board_name:str
    board_id:int

class BoardInfo(BoardBase):
    board_name:str
    star:int
    like:int
    board_id:int
    user_id:int

    
