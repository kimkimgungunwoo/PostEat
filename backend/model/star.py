from sqlalchemy import Boolean, Column,Integer, String,ForeignKey
from sqlalchemy.types import TIMESTAMP,DateTime
from sqlalchemy.sql import text, func
from database import Base
from sqlalchemy.orm import relationship

class Star(Base):
    __tablename__ = "star"
    
    user_id = Column(Integer,ForeignKey("user.id"),nullable=False, index=True, primary_key=True)
    board_id = Column(Integer, ForeignKey("board.board_id"),nullable=False, index=True,  primary_key=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    
    user = relationship("User",backref="stars")
    board = relationship("Board",backref="stars")

# class Star:
#     def __init__(self, board_id:int, user_id:int,created_at:datetime):
#         self.board_id = board_id
#         self.user_id = user_id
#         self.created_at = created_at
