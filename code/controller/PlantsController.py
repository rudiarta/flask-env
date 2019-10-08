from model.PlantsModel import PlantsModel
from app import db
import jwt
import requests
import json

class PlantsController:
    statuscode = 200
    def __init__(self,requestData):
        self.requestData = requestData

    def listAllPlants(self):
        isi = PlantsModel.query.all()
        for x in isi:
            print(x.name)
        
        return {"name":"data.name","category":"data.category"}

    def insertPlants(self):
        requestData = self.requestData
        try:
            data = PlantsModel(requestData.form['name'],requestData.form['category'])
            db.session.add(data)
            db.session.commit()
            return {"name":data.name,"category":data.category}
        except:
            self.statuscode = 406
            return {"message":"error, ..."}