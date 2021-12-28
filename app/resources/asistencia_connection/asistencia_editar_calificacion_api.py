from flask.wrappers import Request
from flask_restful import Resource
from app.models import asistencia_connection
from flask import request, jsonify

class Asistencia_editar_calificacion_api(Resource):
    def get(self):
       return jsonify({"message":"Solo post"})

    def post(self):
        modelo_docente=request.json
        aux_editar_calificacion = asistencia_connection.edit_calificacion(modelo_docente)
        if aux_editar_calificacion == None:
            return jsonify({"message":"No existe la calificacion del docente"})

        return jsonify(aux_editar_calificacion)
    
