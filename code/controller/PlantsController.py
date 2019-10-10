from repository.PlantsRepository import PlantsRepository
from app import db
import jwt
import requests
import json

class PlantsController:
    statuscode = 200
    def __init__(self,requestData):
        self.requestData = requestData

    def listAllPlants(self):
        isi = PlantsRepository.query.all()
        data = {}
        returns = []
        for x in isi:
            data['name'] = x.name
            data['category'] = x.category
            returns.append(data)   
            data = {} 

        return {"plants":returns}

    def insertPlants(self):
        requestData = self.requestData
        try:
            plants = PlantsRepository()
            returns = plants.addPlants(requestData.form['name'],requestData.form['category'])
            return {"name":returns.name,"category":returns.category}
        except:
            self.statuscode = 406
            return {"message":"error, ..."}

    def deletePlants(self):
        requestData = self.requestData
        plants = PlantsRepository()
        returns = plants.deletePlants(requestData.form['id'])
        return {"message":"del"}