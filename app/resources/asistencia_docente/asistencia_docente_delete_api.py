from flask_restful import Resource
from app.models import asistencia_docente
from flask import jsonify, request

class Asistencia_docente_delete_api(Resource):
    def get(self):
        return jsonify({"message":"Solo POST"})    

    def post(self):
        key = request.json
        if asistencia_docente.delete_asistencia_docente(key):
            return jsonify({"message":"Eliminado correctamente"})
        return jsonify({"message":"Error al eliminar"})   

