from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class PlantsOrmModel(Base):
    __tablename__ = 'plants'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    category = Column(String(100))
    
    def __init__(self, name, category):
        self.name = name
        self.category = category