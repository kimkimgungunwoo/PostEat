from schemas import postit_like_schema,board_like_schema
from model.board_like import BoardLike
from model.postit_like import PostItLike
from datetime import datetime
from sqlalchemy import or_
from sqlalchemy.orm import Session

def add_board_like_by_id(board_id,user_id,db:Session):
    existing_like=db.query(BoardLike).filter_by(board_id=board_id,user_id=user_id).first()
    if existing_like:
        return None
    db_board_like=BoardLike(board_id=board_id,user_id=user_id)
    db.add(db_board_like)
    db.commit()
    return db_board_like


def add_postit_like_by_id(postit_id,user_id,db:Session):
    existing_like=db.query(PostItLike).filter_by(postit_id=postit_id).first()
    if existing_like:
        return None
    db_postit_like=PostItLike(postit_id=postit_id,user_id=user_id)
    db.add(db_postit_like)
    db.commit()
    return db_postit_like

