from flask_restful import Resource
from app.models import docente
from flask import jsonify

class Docente_api(Resource):
    def get(self):        
        aux_docentes = docente.get_all_docentes()
        if aux_docentes == None:
            return jsonify({"message":"Ningun Docente"})
        return jsonify(aux_docentes)

    def post(self):
        return jsonify({"message":"Solo GET"})