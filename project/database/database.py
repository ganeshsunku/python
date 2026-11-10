from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

user_name='postgres'
password='postgres'
host='localhost'
port=5432
db_name='postgres'
db_url=f'postgresql+psycopg2://{user_name}:{password}@{host}:{port}/{db_name}'

engine = create_engine(db_url)

session = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
    db= session()
    try:
        yield db
    finally:
        db.close()
