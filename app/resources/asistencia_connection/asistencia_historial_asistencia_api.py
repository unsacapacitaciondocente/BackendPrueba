from flask_restful import Resource
from app.models import asistencia_connection
from flask import jsonify

class Asistencia_historial_asistencia_api(Resource):
    def get(self,id):
        aux_historial_asistencias = asistencia_connection.historial_asistencias(id)
        if aux_historial_asistencias == None:
            return jsonify({"message":"Aun no se han generado asistencias"})

        return jsonify(aux_historial_asistencias)

    def post(self):
        return jsonify({"message":"Solo GET"})
