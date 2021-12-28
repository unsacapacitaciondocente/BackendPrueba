"""
from flask_restful import Resource
from app.models import documento_ponente
from flask import request, jsonify

class Documento_ponente_api(Resource):
    def get(self):        
        aux_documento_grupos = documento_ponente.get_all_documento_ponente()
        if aux_documento_grupos == None:
            return jsonify({"message":"Ningun Docente"})
        return jsonify(aux_documento_grupos)

    def post(self):
        return jsonify({"message":"Solo GET"})
        """