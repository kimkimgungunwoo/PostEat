from schemas import follow_schema
from typing import List
from model.follow import Follow
from datetime import datetime
from sqlalchemy import or_
from sqlalchemy.orm import Session

def follow_user_by_id(user_id,follower_id,db:Session):
    db_follow=Follow(followed_id=user_id,
                      follower_id=follower_id
                      )
    db.add(db_follow)
    db.commit()
    return db_follow


def get_following_list_by_id(user_id,db:Session):
    return db.query(Follow).filter(Follow.follower_id == user_id).all()

def get_follower_list_by_id(user_id, db:Session):
    follower_list = db.query(Follow).filter(Follow.followed_id == user_id).all()

    return follower_list

