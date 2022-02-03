from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

#overall db connection
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)

#generate temporary connections for performing CRUD ops
Session = sessionmaker(bind=engine)

#map models to MySQL tables
Base = declarative_base()