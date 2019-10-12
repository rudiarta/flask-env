from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
import os

# settings.py << use for dotEnv
from dotenv import load_dotenv
load_dotenv()
# OR, the same with increased verbosity: << use for dotEnv
load_dotenv(verbose=True)

engine = create_engine(os.getenv("MYSQL_URL"), echo = True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Plants(Base):
    __tablename__ = 'plants'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    category = Column(String(100))
    def __init__(self, name, category):
        self.name = name
        self.category = category

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()

def addTanaman(name, category):
    c1 = Plants(name, category)
    session.add(c1)
    session.commit()