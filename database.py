from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:sutharsan2203@localhost:3306/HTML-Files"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind = engine)

def db_conn():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()