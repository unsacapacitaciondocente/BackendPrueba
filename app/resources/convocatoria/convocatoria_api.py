from flask_restful import Resource
from app.models import convocatoria
from flask import request, jsonify

class Convocatoria_api(Resource):
    def get(self):        
        aux_convocatoria = convocatoria.all_convocatorias()
        if aux_convocatoria == None:
            return jsonify({"message":"Ninguna Convocatoria"})
        return jsonify(aux_convocatoria)

    def post(self):
        return jsonify({"message":"Solo GET"})