from flask_restful import Resource
from app.models import usuario
from flask import request, jsonify

class Usuario_add_api(Resource):
    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        data = request.json
        if usuario.add_usuario(data):
            return jsonify({"message":"Registrado correctamente"})
        return jsonify({"message":"Error"})