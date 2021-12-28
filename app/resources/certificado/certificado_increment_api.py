from flask_restful import Resource
from app.models import certificado_connection
from flask import request, jsonify

class Certificado_increment_api(Resource):    
    def get(self,id):
        if certificado_connection.incrementDowload(id):
            return jsonify({"message":"Correcto"})
    def post(self):

        return jsonify({"message":"Error"})