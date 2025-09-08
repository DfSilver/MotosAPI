import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.motor_model import Base

SQLITE_URI = 'sqlite:///motorcycles_local.db'

engine = create_engine(SQLITE_URI, echo=True)
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

def get_db_session():
    return Session()
