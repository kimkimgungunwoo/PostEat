from schemas import star_schema
from model.star import Star
from datetime import datetime
from sqlalchemy.orm import Session
from model.board import Board

def add_star_to_board(board_id:int,user_id:int,db:Session):
    db_star=Star(board_id=board_id,user_id=user_id,created_at=datetime.now())
    db.add(db_star)
    db.commit()
    db.refresh(db_star)
    return db_star

def read_star_by_user_id(user_id:int,db:Session):
    return db.query(Star).filter_by(user_id=user_id).all()