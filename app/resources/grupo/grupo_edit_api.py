from flask_restful import Resource
from app.models import grupo
from flask import request, jsonify

class Grupo_edit_api(Resource):
    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        data = request.json
        if grupo.edit_grupo(data):
            return jsonify({"message":"Actualizado correctamente"})
        return jsonify({"message":"Error al actualizar"}) 