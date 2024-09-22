from model.postit import Postit
from schemas import postit_schema
from datetime import datetime
from typing import List, Optional
from sqlalchemy import or_
from sqlalchemy.orm import Session

def add_post_it(board_id:int,postit:postit_schema.PostitCreate,user_id:int,db:Session):
    db_postit=Postit(board_id=board_id,
                  user_id=user_id,
                  content=postit.content,
                  address=postit.address,
                  updated_at=datetime.now(),
                  created_at=datetime.now(),
                  like=0,
                  is_deleted=False
                  )
    db.add(db_postit)
    db.commit()
    db.refresh(db_postit)
    return db_postit

def get_post_list(board_id:int,db:Session) :
    return db.query(Postit).filter_by(board_id=board_id).all()

def get_postits_by_user_id(user_id:int,db:Session):
    return db.query(Postit).filter_by(user_id=user_id).all()

def get_postit_detail_by_id(postit_id:int,db:Session):
    return db.query(Postit).filter_by(postit_id=postit_id).first()

def increase_like(postit_id:int,db:Session):
    db_postit=db.query(Postit).filter_by(postit_id=postit_id).first()
    db_postit.like=db_postit.like+1
    db.commit()
    return db_postit
