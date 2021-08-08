from flask_restful import Resource
from app.models import curso
from flask import request, jsonify

class Curso_add_api(Resource):
    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        data  = request.json
        if curso.add_curso(data):
            return jsonify({"message":"Registrado correctamente"})
        return jsonify({"message":"Error"})
        