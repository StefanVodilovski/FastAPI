from typing import List
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings



# SQLAlchemy specific code, as with any other app
DATABASE_URL = f"mysql+pymysql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(autocommit= False, autoflush =False, bind = engine)

Base = declarative_base()


def get_db():
    db = sessionLocal()
    try: 
        yield db
    finally:
        db.close()  
