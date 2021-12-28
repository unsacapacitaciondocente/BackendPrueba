from flask.wrappers import Request
from flask_restful import Resource
from app.models import asistencia_connection
from flask import request, jsonify

class Asistencia_editar_asistencia_api(Resource):
    def get(self):
       return jsonify({"message":"Solo post"})

    def post(self):
        modelo_docente=request.json
        aux_editar_asistencia = asistencia_connection.edit_asistencia(modelo_docente)
        if aux_editar_asistencia == None:
            return jsonify({"message":"No existe la calificacion del docente"})

        return jsonify(aux_editar_asistencia)
    
