from sqlalchemy import Boolean, Column,Integer, String,ForeignKey
from sqlalchemy.types import TIMESTAMP,DateTime
from sqlalchemy.sql import text, func

from database import Base

from sqlalchemy.orm import relationship

class BoardLike(Base):
    __tablename__ = 'board_like'

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, primary_key=True)
    board_id = Column(Integer, ForeignKey('board.board_id'), nullable=False, primary_key=True)


# class BoardLike:
#     def __init__(self,user_id,board_id):
#         self.user_id = user_id
#         self.board_id = board_id