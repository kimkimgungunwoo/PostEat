from sqlalchemy import Boolean, Column,Integer, String,ForeignKey
from sqlalchemy.types import TIMESTAMP,DateTime
from sqlalchemy.sql import text, func
from datetime import datetime
from database import Base

from sqlalchemy.orm import relationship

class Follow(Base):
    __tablename__ = "follow"
    
    follower_id = Column(Integer, ForeignKey("user.id"),nullable=False, index=True, primary_key=True)
    followed_id = Column(Integer, ForeignKey("user.id"),nullable=False, index=True,  primary_key=True)
    created_at = Column(TIMESTAMP, server_default=func.now())

