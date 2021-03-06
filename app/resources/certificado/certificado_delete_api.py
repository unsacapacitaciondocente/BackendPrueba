from flask_restful import Resource
from app.models import certificado_connection
from flask import jsonify, request

class Certificado_delete_api(Resource):
    def get(self):
        return jsonify({"message":"Solo POST"})           

    def post(self):
        data = request.json
        if certificado_connection.deleteCertificatesByDocente(data) :
            return jsonify({"mensaje":"Cerficados elminados"}) 
        else:
            return jsonify({"mensaje":"Error al generar certificados"}) 