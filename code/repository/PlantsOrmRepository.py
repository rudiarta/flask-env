from model.PlantsOrmModel import PlantsOrmModel
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# settings.py << use for dotEnv
from dotenv import load_dotenv
load_dotenv()
# OR, the same with increased verbosity: << use for dotEnv
load_dotenv(verbose=True)

engine = create_engine(os.getenv("MYSQL_URL"), echo = True)
Session = sessionmaker(bind = engine)
session = Session()

def addTanaman(name, category):
    data = PlantsOrmModel(name, category)
    session.add(data)
    session.commit()