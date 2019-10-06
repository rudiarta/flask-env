from flask import Flask
from controller.UserController import *
import os

app = Flask(__name__)

@app.route('/')
def index():
    u = UserController()
    return u.show()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')