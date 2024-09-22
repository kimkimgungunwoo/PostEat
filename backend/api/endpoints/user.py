from typing import List, Optional
from datetime import datetime,timedelta

from starlette import status

from crud.user_crud import pwd_context
from schemas import user_schema,follow_schema,star_schema,board_schema,postit_schema
from fastapi import Depends, APIRouter, HTTPException, Query
from crud import user_crud, follow_crud, star_crud, board_crud,postit_crud
from api.dep import get_db
from sqlalchemy.orm import Session

from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt,JWTError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/login")

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24
ALGORITHM = "HS256"
SECRET_KEY = "6afaf6ecd05b7696f077916304ca5c0e5ac6c04b8c9b9da48581586d215e9ae3"

router=APIRouter()
@router.post("/login", response_model=user_schema.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                           db: Session = Depends(get_db)):

    # check user and password
    user = user_crud.get_user_by_email(form_data.username,db)
    if not user or not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # make access token
    data = {
        "sub": user.nickname,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "email": user.email,
        "id":user.id
    }
@router.post("/signup", response_model=user_schema.CreateUserResponse)
def signup(user: user_schema.CreateUser,db: Session = Depends(get_db)):
    return user_crud.create_user(user,db)
@router.get("/me")
def get_current_user_info(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    username=get_current_user(token,db)
    user=user_crud.get_user_by_nickname(username,db)
    return {"user_id": user.id}

@router.get("/{user_id}",response_model=user_schema.UserInfo)
def get_user(user_id:int,
             db: Session = Depends(get_db)):
    return user_crud.get_user_by_id(user_id,db)

@router.get("",response_model=List[user_schema.UserInfo])
def search_user(username: Optional[str] = Query(None),db: Session = Depends(get_db)):
    return user_crud.search_user_by_nickname(username,db)


@router.get("/{user_id}/following",response_model=List[user_schema.UserInfo])
def get_following(user_id:int,db: Session = Depends(get_db)):
    following_list=follow_crud.get_following_list_by_id(user_id,db)
    user_list=[user_crud.get_user_by_id(x.followed_id,db) for x in following_list ]
    # return follow_crud.get_following_list_by_id(user_id,db)
    return user_list

@router.get("/{user_id}/follower",response_model=List[user_schema.UserInfo])
def get_follower(user_id:int,db: Session = Depends(get_db)):
    # return follow_crud.get_follower_list_by_id(user_id,db)
    follower_list=follow_crud.get_follower_list_by_id(user_id,db)
    user_list=[user_crud.get_user_by_id(x.follower_id,db) for x in follower_list ]
    return user_list
@router.post("/{user_id}/follow",response_model=follow_schema.FollowInfo)
def follow_user(user_id:int,follower_id:int,db: Session = Depends(get_db)):
    user_crud.increase_followers(user_id,db)
    user_crud.increase_following(follower_id,db)
    return follow_crud.follow_user_by_id(user_id,follower_id,db)

@router.get("/{user_id}/star",response_model=List[star_schema.starInfo])
def read_star(user_id:int,db: Session = Depends(get_db)):
    return star_crud.read_star_by_user_id(user_id,db)

@router.get("/{user_id}/boards",response_model=List[board_schema.BoardInfo])
def read_boards(user_id:int,db: Session = Depends(get_db)):
    return board_crud.get_board_by_user_id(user_id,db)

@router.get("/{user_id}/postit",response_model=List[postit_schema.PostitInfo])
def read_postits(user_id:int,db: Session = Depends(get_db)):
    return postit_crud.get_postits_by_user_id(user_id,db)




def get_current_user(token: str = Depends(oauth2_scheme),
                        db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # JWT 토큰에서 payload를 디코딩합니다.
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # payload에서 user_id를 추출합니다. ('sub' 필드에서 추출)
        user_nickname = payload.get("sub")

        # user_id가 없으면 인증 오류를 발생시킵니다.
        if user_nickname is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    # 추출한 user_id를 반환합니다.
    return user_nickname




