from flask_restful import Resource
from app.models import asistencia
from flask import jsonify, request

class Asistencia_delete_api(Resource):
    def get(self):
        return jsonify({"message":"Solo POST"})    

    def post(self):
        key = request.json
        if asistencia.delete_asistencia(key):
            return jsonify({"message":"Eliminado correctamente"})
        return jsonify({"message":"Error al eliminar"})  

