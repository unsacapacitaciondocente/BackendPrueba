from flask_restful import Resource
from app.models import certificado
from flask import request, jsonify

class Certificado_add_api(Resource):
    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        data  = request.json
        if certificado.add_certificado(data):
            return jsonify({"message":"Registrado correctamente"})
        return jsonify({"message":"Error"})