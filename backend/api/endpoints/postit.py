from typing import List
from datetime import timedelta
from schemas import user_schema,board_schema,postit_schema
from fastapi import Depends, APIRouter, HTTPException
from schemas import board_schema,postit_schema,star_schema,postit_like_schema
from crud import postit_crud,like_crud
from api.dep import get_db
from sqlalchemy.orm import Session

router=APIRouter()


@router.get("/{postit_id}/detail",response_model=postit_schema.PostItDetail)
def postit_detail(postit_id:int,db:Session=Depends(get_db)):
    return postit_crud.get_postit_detail_by_id(postit_id,db)
@router.post("/{postit_id}/like",response_model=postit_like_schema.PostItLikeInfo)
def postit_like(postit_id:int,user_id:int,db:Session=Depends(get_db)):
    postit_crud.increase_like(postit_id,db)
    return like_crud.add_postit_like_by_id(postit_id,user_id,db)



