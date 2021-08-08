from flask_restful import Resource
from app.models import curso
from flask import jsonify, request
class Curso_detalle_api(Resource):
    def get(self,id):
        return jsonify(curso.detalle_curso(id))           

    def post(self):
        return jsonify({"message":"Solo GET"})