from flask import Flask, jsonify, request, make_response
from controller.ArticleController import *

app = Flask(__name__)

@app.route('/', methods=['POST'])
def listAllArticle():
    controller = ArticleController(request,app)
    return make_response(controller.listAllArticle(), controller.statuscode)

@app.route('/insert', methods=['POST'])
def insertArticle():
    controller = ArticleController(request,app)
    return make_response(controller.insertArticle(), controller.statuscode)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')