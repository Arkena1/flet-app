from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
SQL_URL = "info.db"

engine = create_engine("sqlite:///"+SQL_URL, connect_args={'check_same_thread': False})

Session = sessionmaker(bind=engine,autocommit=False, autoflush=False,)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()