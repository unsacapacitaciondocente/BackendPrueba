from flask_restful import Resource
from app.models import configuracion
from flask import jsonify, request
class Configuracion_detalle_api(Resource):
    def get(self,id):
        return jsonify(configuracion.detalle_configuracion(id))          

    def post(self):
        return jsonify({"message":"Solo GET"})