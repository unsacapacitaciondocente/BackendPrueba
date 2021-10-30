from flask_restful import Resource
from app.models import asistencia_docente
from flask import jsonify

class Asistencia_docente_api(Resource):
    def get(self):
        
        aux_asistencia_docentes = asistencia_docente.get_all_asistencia_docente()
        if aux_asistencia_docentes == None:
            return jsonify({"message":"Ningun curso"})

        return jsonify(asistencia_docente.get_all_asistencia_docente())

    def post(self):
        return jsonify({"message":"Solo GET"})