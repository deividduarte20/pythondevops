from flask import flask
from flask import Resource, Api

app = Flask(_name_)
api = Api(app)

class Hoteis(Resource):
    def get(self):