from flask_restful import Resource
from app.models import resolucion
from flask import request, jsonify

class Resolucion_detalle_api(Resource):
    
    def get(self, id):
        return jsonify(resolucion.detalle_resolucion(id))
    def post(self):
        return jsonify({"message":"Solo GET"})