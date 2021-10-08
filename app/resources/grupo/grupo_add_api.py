from flask_restful import Resource
from app.models import grupo
from flask import request, jsonify

class Grupo_add_api(Resource):
    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        data  = request.json
        if grupo.add_grupo(data):
            return jsonify({"message":"Registrado correctamente"})
        return jsonify({"message":"Error"})