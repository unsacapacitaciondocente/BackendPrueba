from flask_restful import Resource
from app.models import asistencia_docente
from flask import request, jsonify

class Asistencia_docente_add_api(Resource):
    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        data  = request.json
        if asistencia_docente.add_asistencia_docente(data):
            return jsonify({"message":"Registrado correctamente"})
        return jsonify({"message":"Error"})
        