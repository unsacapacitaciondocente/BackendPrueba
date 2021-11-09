from flask_restful import Resource
from app.models import certificado
from flask import jsonify, request
class Certificado_detalle_api(Resource):
    def get(self):
        data =request.json
        return jsonify(certificado.all_certificados_by_usuario(data))           

    def post(self):
        return jsonify({"message":"Solo GET"})