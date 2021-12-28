
"""
from flask_restful import Resource
from app.models import documento_ponente
from flask import request, jsonify

class Documento_ponente_detalle_api(Resource):    
    def get(self,id):
        return jsonify(documento_ponente.detalle_documento_ponente(id))
    def post(self):
        return jsonify({"message":"Error"})
        """