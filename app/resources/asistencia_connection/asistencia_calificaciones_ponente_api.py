from flask_restful import Resource
from app.models import asistencia_connection
from flask import jsonify

class Asistencia_calificaciones_ponente_api(Resource):
    def get(self,id):
        aux_calificaciones_docente= asistencia_connection.calificaciones_docente(id)
        if aux_calificaciones_docente == None:
            return jsonify({"message":"Aun no se han generado calificaciones"})

        return jsonify(aux_calificaciones_docente)

    def post(self):
        return jsonify({"message":"Solo GET"})
