from flask_restful import Resource
from app.models import grupo
from flask import request, jsonify

class Grupo_delete_api(Resource):    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        key = request.json
        if grupo.delete_grupo(key):
            return jsonify({"message":"Eliminado correctamente"})
        return jsonify({"message":"Error al eliminar"}) 