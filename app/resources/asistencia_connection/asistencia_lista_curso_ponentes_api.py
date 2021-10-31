from flask_restful import Resource
from app.models import asistencia_connection
from flask import jsonify

class Asistencia_lista_curso_ponentes_api(Resource):
    def get(self,id):
        aux_lista_curso = asistencia_connection.lista_cursos_ponente(id)
        if aux_lista_curso == None:
            return jsonify({"message":"No existe cursos asociados al docente"})

        return jsonify(aux_lista_curso)

    def post(self):
        return jsonify({"message":"Solo GET"})