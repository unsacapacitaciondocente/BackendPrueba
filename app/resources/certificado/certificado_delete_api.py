from flask_restful import Resource
from app.models import certificado
from flask import jsonify, request

class Certificado_delete_api(Resource):
    def get(self):
        return jsonify({"message":"Solo POST"})    

    def post(self):
        key = request.json
        if certificado.delete_certificado(key):
            return jsonify({"message":"Eliminado correctamente"})
        return jsonify({"message":"Error al eliminar"})   
