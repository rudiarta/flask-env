from flask import Flask, jsonify, request, make_response
from controller.PlantsController import *
from middleware.authJwtMiddleware import authJwtMiddleware
from flask_sqlalchemy import SQLAlchemy
import os

# Database init
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("MYSQL_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def listAllPlants():
    controller =  authJwtMiddleware(PlantsController(request), request.headers['x-access-token']).handle()
    try:
        result = make_response(controller.listAllPlants(), controller.statuscode)
    except:
        result = make_response(controller, 401)
    return result

@app.route('/limit/<int:post_id>', methods=['GET'])
def listLimitPlants(post_id):
    controller = PlantsController(request)
    return make_response(controller.listLimitPlants(post_id), controller.statuscode)

@app.route('/insert', methods=['POST'])
def insertPlants():
    controller = PlantsController(request)
    return make_response(controller.insertPlants(), controller.statuscode)

@app.route('/insert/cache', methods=['POST'])
def insertPlantsQueue():
    controller = PlantsController(request)
    return make_response(controller.insertWithCache(), controller.statuscode)

@app.route('/delete/<int:post_id>', methods=['GET'])
def deletePlants(post_id):
    controller = PlantsController(request)
    return make_response(controller.deletePlants(post_id), controller.statuscode)

@app.route('/update/<int:post_id>', methods=['POST'])
def updatePlants(post_id):
    controller = PlantsController(request)
    return make_response(controller.updatePlants(post_id), controller.statuscode)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')