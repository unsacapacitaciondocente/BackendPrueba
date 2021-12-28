from flask_restful import Resource
from app.models import asistencia
from flask import request, jsonify

class Asistencia_add_api(Resource):
    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        data  = request.json
        if asistencia.add_asistencia(data):
            return jsonify({"message":"Registrado correctamente"})
        return jsonify({"message":"Error, no se pudo agregar"})