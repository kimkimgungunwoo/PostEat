from sqlalchemy import Boolean, Column,Integer, String,ForeignKey
from sqlalchemy.types import TIMESTAMP,DateTime
from sqlalchemy.sql import text, func
from database import Base
from sqlalchemy.orm import relationship

class PostItLike(Base):
    __tablename__ = 'postit_like'

    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    postit_id = Column(Integer, ForeignKey('postit.postit_id'), primary_key=True)

    user=relationship('User')




# class PostItLike:
#     def __init__(self,user_id,postit_id):
#         self.user_id = user_id
#         self.postit_id = postit_id
