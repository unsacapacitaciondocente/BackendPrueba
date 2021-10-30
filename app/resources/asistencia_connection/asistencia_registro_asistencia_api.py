from flask_restful import Resource
from app.models import asistencia_connection
from flask import jsonify

class Asistencia_registro_asistencia_api(Resource):
    def get(self,id):
        #el "id" debe de pertenecer de la entidad "asistencia_id" 
        aux_lista_docentes = asistencia_connection.registro_asistencias(id)
        if aux_lista_docentes == None:
            return jsonify({"message":"No existen docentes asociados a este grupo-curso"})

        return jsonify(aux_lista_docentes)

    def post(self):
        return jsonify({"message":"Solo GET"})