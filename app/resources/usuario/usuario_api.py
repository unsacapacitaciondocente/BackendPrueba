from flask_restful import Resource
from app.models import usuario
from flask import jsonify

class Usuario_api(Resource):
    def get(self):        
        aux_usuario = usuario.get_all_usuarios()
        if aux_usuario == None:
            return jsonify({"message":"Ningun Docente"})
        return jsonify(aux_usuario)

    def post(self):
        return jsonify({"message":"Solo GET"})