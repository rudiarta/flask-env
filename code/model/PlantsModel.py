from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db

class PlantsModel(db.Model):
    __tablename__ = "plants"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(100))

    def __init__(self, name, category):
        self.name = name
        self.category = category