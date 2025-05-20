# Database migration and model definition
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AnonymousUser(Base):
    __tablename__ = "anonymous_users"
    
    id = Column(Integer, primary_key=True)
    anonymous_identifier = Column(String, unique=True)
    perspective_count = Column(Integer, default=0)
