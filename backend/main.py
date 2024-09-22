from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.api import api_router
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="PostEat")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 출처 허용
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메소드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)

app.include_router(api_router, prefix="/api")
