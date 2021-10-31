from flask_restful import Resource
from app.models import curso_seguimiento
from flask import jsonify

class Curso_seguimiento_api(Resource):
    def get(self):

        aux_cursos_seguimiento = curso_seguimiento.get_cursos_seguimiento()
        if aux_cursos_seguimiento == None:
            return jsonify({"message":"Ningun curso en seguimiento"})

        return jsonify(aux_cursos_seguimiento)

    def post(self):
        return jsonify({"message":"Solo GET"})