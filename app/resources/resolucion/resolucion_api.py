from flask_restful import Resource
from app.models import resolucion
from flask import jsonify

class Resolucion_api(Resource):
    def get(self):        
        aux_resoluciones = resolucion.get_all_resoluciones()
        if aux_resoluciones == None:
            return jsonify({"message":"Ningun ponente"})
        return jsonify(aux_resoluciones)

    def post(self):
        return jsonify({"message":"Solo GET"})

