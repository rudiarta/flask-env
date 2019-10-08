from flask import Flask, jsonify, request, make_response
from controller.PlantsController import *

app = Flask(__name__)

@app.route('/', methods=['POST'])
def listAllArticle():
    controller = PlantsController(request,app)
    return make_response(controller.listAllPlants(), controller.statuscode)

@app.route('/insert', methods=['POST'])
def insertArticle():
    controller = PlantsController(request,app)
    return make_response(controller.insertPlants(), controller.statuscode)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')