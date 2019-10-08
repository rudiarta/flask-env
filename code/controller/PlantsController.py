from model.PlantsModel import *
import jwt
import requests
import json

class PlantsController:
    statuscode = 200
    def __init__(self,requestData,appData):
        self.requestData = requestData
        self.appData = appData

    def listAllPlants(self):
        x = ArticleModel()
        y = self.requestData.get_json()
        y = json.dumps(y)
        y = json.loads(y)
        return {"name":y["name"]}

    def insertPlants(self):
        requestData = self.requestData
        try:
            x = int(requestData.form['number'])
            result = x * 2
            return {"sum":result}
        except:
            self.statuscode = 406
            return {"message":"error, params not integer"}