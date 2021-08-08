from flask_restful import Resource
from app.models import ponente
from flask import jsonify

class Ponente_api(Resource):
    def get(self):        
        aux_ponentes = ponente.get_all_ponentes()
        if aux_ponentes == None:
            return jsonify({"message":"Ningun ponente"})
        return jsonify(aux_ponentes)

    def post(self):
        return jsonify({"message":"Solo GET"})

