from flask_restful import Resource
from app.models import certificado
from flask import jsonify, request

class Certificado_all_api(Resource):
    def get(self):
        return jsonify({"message":"Solo POST"})          

    def post(self):
        data =request.json
        return jsonify(certificado.all_certificados_by_usuario(data))  
        