from flask_restful import Resource
from app.models import ponente
from flask import request, jsonify

class Ponente_detalle_api(Resource):
    
    def get(self, id):
        return jsonify(ponente.detalle_ponente(id))
    def post(self):
        return jsonify({"message":"Solo GET"})

