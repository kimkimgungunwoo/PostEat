from typing import List,Optional
from datetime import timedelta
from schemas import user_schema,board_schema,postit_schema,star_schema,board_like_schema
from fastapi import Depends, APIRouter, HTTPException,Query
from crud import board_crud,postit_crud,star_crud,like_crud
from api.dep import get_db
from sqlalchemy.orm import Session
router=APIRouter()

@router.post("",response_model=board_schema.BoardCreateResponse)
def create_board(board:board_schema.BoardCreate,user_id:int,db:Session=Depends(get_db)):
    created_board=board_crud.create_board(board,user_id,db)
    return created_board

@router.get("",response_model=List[board_schema.BoardInfo])
def read_all_board(db:Session=Depends(get_db)):
    return board_crud.read_all_board(db)
# @router.get("",response_model=List[board_schema.BoardInfo])
# def search_board(board_title:Optional[str]= Query(None,min_length=0),db:Session=Depends(get_db)):
#     return board_crud.search_board_by_title(board_title,db)

# @router.get("/{board_id}",response_model=board_schema.BoardInfo)
# def get_board(board_id:int,db:Session=Depends(get_db)):
#     return board_crud.get_board_by_id(board_id,db)

@router.get("/{board_id}/postit",response_model=List[postit_schema.PostitInfo])
def get_postit(board_id:int,db:Session=Depends(get_db)):
    return postit_crud.get_post_list(board_id,db)


@router.post("/{board_id}/postit",response_model=postit_schema.PostitInfo)
def post_postit(board_id:int,postit:postit_schema.PostitCreate,user_id:int,db:Session=Depends(get_db)):
    return postit_crud.add_post_it(board_id,postit,user_id,db)


@router.post("/{board_id}/star",response_model=star_schema.starInfo)
def add_star(board_id:int,user_id:int,db:Session=Depends(get_db)):
    board_crud.increase_star(board_id,db)
    return star_crud.add_star_to_board(board_id,user_id,db)


@router.post("/{board_id}/like",response_model=board_like_schema.BoardLikeInfo)
def like(board_id:int,user_id:int,db:Session=Depends(get_db)):
    board_crud.add_like(board_id,db)
    return like_crud.add_board_like_by_id(board_id,user_id,db)





