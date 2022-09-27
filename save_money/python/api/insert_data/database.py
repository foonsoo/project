from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql
import os

# Database connection
username = os.environ['username']
password = os.environ['password']
host = os.environ['host']
port = os.environ['port']
database = os.environ['database']

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

