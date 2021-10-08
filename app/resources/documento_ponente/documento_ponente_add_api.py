from flask_restful import Resource
from app.models import documento_ponente
from flask import request, jsonify

class Documento_ponente_add_api(Resource):
    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        data  = request.json
        if documento_ponente.add_documento_ponente(data):
            return jsonify({"message":"Registrado correctamente"})
        return jsonify({"message":"Error"})