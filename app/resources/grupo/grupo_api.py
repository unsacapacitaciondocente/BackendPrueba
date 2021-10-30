from flask_restful import Resource
from app.models import grupo
from flask import jsonify

class Grupo_api(Resource):
    def get(self):        
        aux_grupos = grupo.get_all_grupo()
        if aux_grupos == None:
            return jsonify({"message":"Ningun Docente"})
        return jsonify(aux_grupos)

    def post(self):
        return jsonify({"message":"Solo GET"})