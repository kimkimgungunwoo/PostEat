
from sqlalchemy import Boolean, Column,Integer, String,ForeignKey
from sqlalchemy.types import TIMESTAMP,DateTime
from sqlalchemy.sql import text, func
from database import Base
from sqlalchemy.orm import relationship



class Postit(Base):
    __tablename__="postit"
    
    postit_id=Column(Integer,nullable=False,index=True,primary_key=True,autoincrement=True)
    created_at=Column(TIMESTAMP,server_default=func.now())
    updated_at = Column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )
    like=Column(Integer,index=True)
    content=Column(String(128),nullable=True)
    address=Column(String(128),nullable=False)
    is_deleted=Column(Boolean,default=False,nullable=False)
    
    user_id=Column(Integer,ForeignKey("user.id"),nullable=False,index=True)
    board_id=Column(Integer,ForeignKey("board.board_id"),nullable=False,index=True)
    
    user=relationship("User",backref="postit")
    board=relationship("Board",backref="postit")

# class Postit:
#     def __init__(self,postit_id:int,created_at:datetime,updated_at:datetime,
#                  like:int,content:str,address:str,is_deleted:bool,user_id:int,board_id:int) :
#         self.postit_id=postit_id
#         self.created_at=created_at
#         self.updated_at=updated_at
#         self.like=like
#         self.content=content
#         self.address=address
#         self.is_deleted=is_deleted
#         self.user_id=user_id
#         self.board_id=board_id
