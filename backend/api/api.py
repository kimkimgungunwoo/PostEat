from api.endpoints import user,postit,board
from fastapi import APIRouter
api_router=APIRouter()

api_router.include_router(user.router,prefix='/user',tags=['user'])
api_router.include_router(postit.router,prefix='/postit',tags=['postit'])
api_router.include_router(board.router,prefix='/board',tags=['board'])
