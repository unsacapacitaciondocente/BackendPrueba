from flask_restful import Resource
from flask import jsonify

class Index(Resource):
    def get(self):
        return jsonify({"message":"welcome to this API V2! GET METHOD"})
    def post(self):
        return jsonify({"message":"welcome to this API V2! POST METHOD"})