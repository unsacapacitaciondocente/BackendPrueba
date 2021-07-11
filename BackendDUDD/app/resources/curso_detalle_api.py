from flask_restful import Resource
from app.models import curso
from flask import jsonify, request

class Curso_detalle_api(Resource):
    def get(self):
        return jsonify({"message":"Solo POST"})    

    def post(self):
        key = request.json
        return jsonify(curso.detalle_curso(key))