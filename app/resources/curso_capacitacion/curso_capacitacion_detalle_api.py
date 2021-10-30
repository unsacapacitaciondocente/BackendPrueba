from flask_restful import Resource
from app.models import curso_capacitacion
from flask import jsonify, request
class Curso_capacitacion_detalle_api(Resource):
    def get(self,id):
        return jsonify(curso_capacitacion.detalle_curso_capacitacion(id))           

    def post(self):
        return jsonify({"message":"Solo GET"})