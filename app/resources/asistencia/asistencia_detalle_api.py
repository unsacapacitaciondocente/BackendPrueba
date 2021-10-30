from flask_restful import Resource
from app.models import asistencia
from flask import jsonify, request
class Asistencia_detalle_api(Resource):
    def get(self,id):
        return jsonify(asistencia.detalle_asistencia(id))           

    def post(self):
        return jsonify({"message":"Solo GET"})