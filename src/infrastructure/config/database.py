from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.infrastructure.config.contants import DB_CONNECTION

engine = create_engine(DB_CONNECTION)


def create_session():
    Session = sessionmaker(bind=engine)
    return Session()
