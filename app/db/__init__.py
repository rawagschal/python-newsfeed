from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g

load_dotenv()

#overall db connection
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)

#generate temporary connections for performing CRUD ops
Session = sessionmaker(bind=engine)

#map models to MySQL tables
Base = declarative_base()

#initialize db
def init_db(app):
    Base.metadata.create_all(engine)

    app.teardown_appcontext(close_db)

#return new session-connection object here so new ones aren't created on each route
def get_db():
    if 'db' not in g:
        # confirm  db connection is stored in app context
        g.db = Session()
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()