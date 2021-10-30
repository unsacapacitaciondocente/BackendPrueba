from flask_restful import Resource
from app.models import asistencia
from flask import jsonify

class Asistencia_api(Resource):
    def get(self):
        
        aux_asistencias = asistencia.get_all_asistencia()
        if aux_asistencias == None:
            return jsonify({"message":"Ningun curso"})

        return jsonify(asistencia.get_all_asistencia())

    def post(self):
        return jsonify({"message":"Solo GET"})