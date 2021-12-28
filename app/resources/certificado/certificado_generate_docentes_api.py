from flask_restful import Resource
from app.models import certificado_connection
from flask import jsonify, request

class Certificado_generate_docentes_api(Resource):
    def get(self):
        return jsonify({"message":"Solo POST"})           

    def post(self):
        data = request.json
        if certificado_connection.generate_certificados_docentes(data) :
            return jsonify({"mensaje":"Generados Certificados"}) 
        else:
            return jsonify({"mensaje":"Error al generar certificados"}) 