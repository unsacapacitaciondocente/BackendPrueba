from flask_restful import Resource
from app.models import usuario
from flask import request, jsonify

class Usuario_edit_api(Resource):
    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        data = request.json

        if usuario.edit_usuario(data):
            return jsonify({"message":"Actualizado correctamente"})
        return jsonify({"message":"Error al actualizar"}) 