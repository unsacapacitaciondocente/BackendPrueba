from flask_restful import Resource
from app.models import usuario
from flask import request, jsonify

class Usuario_delete_api(Resource):    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        key = request.json
        if usuario.delete_usuario(key):
            return jsonify({"message":"Eliminado correctamente"})
        return jsonify({"message":"Error al eliminar"}) 