from flask.wrappers import Request
from flask_restful import Resource
from app.models import asistencia_connection
from flask import request, jsonify

class Asistencia_guardar_registro_asistencia_api(Resource):
    def get(self):
       return jsonify({"message":"Solo post"})

    def post(self):
        modelo_docente=request.json
        aux_editar_calificacion = asistencia_connection.guardar_registro_asistencia(modelo_docente)
        if aux_editar_calificacion == None:
            return jsonify({"message":"No se pudieron guardar los registros"})

        return jsonify({"message":"Se guardo correctamente"})
    