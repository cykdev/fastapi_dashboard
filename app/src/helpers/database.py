# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from app.src.config import settings
from src.config import settings

SQLITE_DATABASE_URL = "sqlite:///./src/sql_app.db"
#MYSQL_DATABASE_URL = f"mysql://{settings.database_username}:{settings.database_password}@{settings.database_port}/{settings.database_name}"
POSTGRESQL_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

if (settings.debugging): #debugging==1
    engine = create_engine(SQLITE_DATABASE_URL, connect_args={'check_same_thread': False})
else: #debugging==0
    engine = create_engine(POSTGRESQL_DATABASE_URL)
    #engine = create_engine(MYSQL_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
