from flask_restful import Resource
from app.models import asistencia
from flask import jsonify, request

class Asistencia_edit_api(Resource):
    def get(self):
        return jsonify({"message":"Solo POST"})    

    def post(self):
        data = request.json
        if asistencia.edit_asistencia(data):
            return jsonify({"message":"Actualizado correctamente"})
        return jsonify({"message":"Error al actualizar"}) 
        