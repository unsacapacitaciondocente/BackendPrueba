from flask_restful import Resource
from app.models import reportes
from flask import request, jsonify

class Cursos_by_ponente_api(Resource):
    def get(self, id):
        aux_cursos_by_ponente = reportes.get_cursos_by_docente(id)
        if aux_cursos_by_ponente == None:
            return jsonify({"message":"Ningun curso"})
        return jsonify(aux_cursos_by_ponente)

    def post(self):
        return jsonify({"message":"Solo GET"})