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
        # isi = PlantsRepository.query.limit(4).all()
        data = {}
        returns = []
        for x in isi:
            data['name'] = x.name
            data['category'] = x.category
            returns.append(data)   
            data = {} 

        return {"plants":returns}

    def listLimitPlants(self, post_id):
        isi = PlantsRepository.query.limit(post_id).all()
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
            return {"message":"error, while inserting ..."}

    def deletePlants(self, post_id):
        requestData = self.requestData
        plants = PlantsRepository()
        returns = plants.deletePlants(post_id)
        if(returns==1):
            return {"message":  "id: "+str(post_id)+" deleted"}
        self.statuscode = 406
        return {"message":"data not found"}

    def updatePlants(self, post_id):
        requestData = self.requestData
        plants = PlantsRepository()
        returns = plants.updatePlants(post_id,requestData.form['name'],requestData.form['category']) 
        if(returns==True):
            return {"message":"update"}
        self.statuscode = 406
        return {"message":"data not found"}