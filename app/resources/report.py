from flask_restful import Resource
from flask import jsonify

class Report(Resource):
    def get(self):
        return jsonify([weather])
    def post(self):
        return jsonify({"message":"This module has no post. That was a test!"})

