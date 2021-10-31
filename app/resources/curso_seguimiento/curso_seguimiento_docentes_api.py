from flask_restful import Resource
from app.models import curso_seguimiento
from flask import jsonify

class Curso_seguimiento_docentes_api(Resource):
    def get(self, id):

        aux_docentes_por_curso = curso_seguimiento.get_docentes_por_curso(id)
        if aux_docentes_por_curso == None:
            return jsonify({"message":"Ningun docente en este curso"})

        return jsonify(aux_docentes_por_curso)

    def post(self):
        return jsonify({"message":"Solo GET"})