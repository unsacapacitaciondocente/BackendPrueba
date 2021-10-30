from flask_restful import Resource
from app.models import asistencia
from app.models import asistencia_connection
from flask import jsonify

class Asistencia_curso_api(Resource):
    def get(self,id):
        aux_asistencia_curso = asistencia_connection.group_for_assistance(id)
        if aux_asistencia_curso == None:
            return jsonify({"message":"No existe el Grupo"})

        return jsonify(aux_asistencia_curso)

    def post(self):
        return jsonify({"message":"Solo GET"})