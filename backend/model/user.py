from sqlalchemy import Boolean, Column,Integer, String,ForeignKey
from sqlalchemy.types import TIMESTAMP,DateTime
from sqlalchemy.sql import text, func
from database import Base
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__="user"
    
    id=Column(Integer,primary_key=True,index=True,nullable=False,unique=True,autoincrement=True)
    nickname=Column(String(32),index=True,nullable=False,unique=True)
    password=Column(String(255),nullable=False)
    created_at=Column(TIMESTAMP,server_default=func.now())
    updated_at = Column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )
    follower=Column(Integer)
    following=Column(Integer)
    email=Column(String(32),index=True)



# class User:
#     def __init__(self,nickname,password,created_at,updated_at,follower,following,email,id):
#         self.nickname=nickname
#         self.password=password
#         self.created_at=created_at
#         self.updated_at=updated_at
#         self.follower=follower
#         self.following=following
#         self.email=email
#         self.id=id

