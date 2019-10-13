from model.PlantsModel import PlantsModel
from main import db

class PlantsRepository(PlantsModel):
    def __init__(self):
        pass

    def addPlants(name, category):
        data = PlantsModel(name, category)
        db.session.add(data)
        db.session.commit()
        print(data.id)
        return data

    def updatePlants(x, name, category):
        plants = PlantsModel.query.filter_by(id=x).first()
        if not plants:
            return False
        plants.name = name
        plants.category = category
        db.session.commit()
        return True

    def deletePlants(x):
        data = PlantsModel.query.filter_by(id=x).delete()
        db.session.commit()
        return data