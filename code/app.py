from flask import Flask, jsonify, request, make_response
from controller.PlantsController import *
from flask_sqlalchemy import SQLAlchemy
import os

# Database init
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("MYSQL_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def listAllPlants():
    controller = PlantsController(request)
    return make_response(controller.listAllPlants(), controller.statuscode)

@app.route('/insert', methods=['POST'])
def insertPlants():
    controller = PlantsController(request)
    return make_response(controller.insertPlants(), controller.statuscode)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')