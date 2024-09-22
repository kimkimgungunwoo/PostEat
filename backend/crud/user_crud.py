from typing import List
from schemas import user_schema,board_schema,postit_schema,follow_schema
from model.user import User
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import or_
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(user: user_schema.CreateUser,db:Session):
    db_user=User(nickname=user.nickname,
                      password=pwd_context.hash(user.password1),
                      email=user.email,
                      created_at=datetime.now(),
                      updated_at=datetime.now(),
                      follower=0,
                      following=0
                      )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(user_id: int,db:Session):
    return db.query(User).filter_by(id=user_id).first()

def search_user_by_nickname(nickname,db:Session):
    return db.query(User).filter(or_(User.nickname.ilike(f"%{nickname}%"))).all()


def increase_following(userid:int,db:Session):
    db_user=get_user_by_id(userid,db)
    db_user.following+=1
    db.commit()
    return db_user


def increase_followers(userid:int,db:Session):
    db_user=get_user_by_id(userid,db)
    db_user.follower+=1
    db.commit()
    return db_user

def get_user_by_email(email:str,db:Session):
    return db.query(User).filter_by(email=email).first()

def get_user_by_nickname(nickname:str,db:Session):
    return db.query(User).filter_by(nickname=nickname).first()