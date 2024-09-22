from typing import List, Optional
from datetime import datetime
from model.postit import Postit
from schemas import board_schema
from model.board import Board
from sqlalchemy.orm import Session
from model.user import User

def create_board(board: board_schema.BoardCreate, user_id: int, db: Session) -> Board:
    db_board = Board(
        user_id=user_id,
        board_name=board.board_name,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        like=0,
        star=0,
        is_deleted=False
    )
    db.add(db_board)
    db.commit()
    db.refresh(db_board)
    return db_board

def read_all_board(db: Session):
    return db.query(Board).all()


def search_board_by_title(board_title: str, db: Session):
    return db.query(Board).filter(Board.board_name.ilike(f"%{board_title}%")).all()

def get_board_by_id(board_id: int, db: Session) -> Optional[Board]:
    return db.query(Board).filter_by(board_id = board_id).first()  # Corrected filter condition

def get_postit_on_board(board_id: int, db: Session) -> Optional[Postit]:
    return db.query(Postit).filter_by(board_id=board_id).first()

def add_like(board_id: int, db: Session):
    board = db.query(Board).filter_by(board_id=board_id).first()
    if board:
        board.like += 1
        db.commit()
    return board

def get_board_by_user_id(user_id: int, db: Session):
    return db.query(Board).filter_by(user_id = user_id).all()

def increase_star(board_id: int, db: Session):
    board = db.query(Board).filter_by(board_id=board_id).first()
    if board:
        board.star += 1
        db.commit()
    return board

# def get_boards_with_username(db: Session):
#     query = db.query(
#         Board.board_name,
#         Board.star,
#         Board.like,
#         Board.board_id,
#         Board.user_id,
#         User.nickname
#     ).join(User, Board.user_id == User.id)
#     return query
