
from sqlalchemy import Boolean, Column,Integer, String,ForeignKey
from sqlalchemy.types import TIMESTAMP,DateTime
from sqlalchemy.sql import text, func

from database import Base

from sqlalchemy.orm import relationship 

class Board(Base):
    __tablename__="board"
    
    board_id=Column(Integer,primary_key=True,nullable=False,index=True,unique=True,autoincrement=True)
    board_name=Column(String(32),nullable=False,index=True)
    created_at=Column(TIMESTAMP,server_default=func.now())
    updated_at = Column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )
    is_deleted=Column(Boolean,default=False,nullable=False)
    star=Column(Integer,index=True)
    like=Column(Integer,index=True)
    
    user_id=Column(Integer,ForeignKey("user.id"),index=True)
    
    
    user=relationship("User",backref="board") #유저에서 board에 접근가능하게 만드는 거


# class Board:
#     def __init__(self,board_id:int,board_name:str,
#                  created_at:datetime,updated_at:datetime,
#                  is_deleted:bool,star:int,like:int,user_id:int):
#         self.board_id=board_id
#         self.board_name=board_name
#         self.created_at=created_at
#         self.updated_at=updated_at
#         self.is_deleted=is_deleted
#         self.star=star
#         self.like=like
#         self.user_id=user_id
