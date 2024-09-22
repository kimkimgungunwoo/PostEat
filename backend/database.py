from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
DB_URL='mysql+pymysql://kimgunwoo:717978@localhost:3306/posteat'
engine = create_engine(DB_URL)

SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)
