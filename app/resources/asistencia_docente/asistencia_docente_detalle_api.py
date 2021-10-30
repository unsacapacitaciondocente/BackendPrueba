from flask_restful import Resource
from app.models import asistencia_docente
from flask import jsonify, request
class Asistencia_docente_detalle_api(Resource):
    def get(self,id):
        return jsonify(asistencia_docente.detalle_asistencia_docente(id))           

    def post(self):
        return jsonify({"message":"Solo GET"})