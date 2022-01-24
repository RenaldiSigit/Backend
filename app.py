from logging import error
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import json

app = Flask(__name__)
api = Api(app)

class home(Resource):
    def get(self):
        sc = open("home.json","r")
        data = json.load(sc)
        return data

class receipe(Resource):
    def get(self):
        sc = open("receipe.json","r")
        data = json.load(sc)
        return data

class contact(Resource):
    def get(self):
        sc = open("contact.json","r")
        data = json.load(sc)
        return data

api.add_resource(home, '/home/')
api.add_resource(receipe,'/receipe/')
api.add_resource(contact,'/contact/')

@app.errorhandler(404)
def page_not_found(e):
    return {"error":"File Not Found"}, 404

if __name__ == '__main__':
    app.run(debug=True,port=5005)