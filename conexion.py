from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:19dejulio@localhost/slangs')
session_create = sessionmaker(bind=engine)

base = declarative_base()