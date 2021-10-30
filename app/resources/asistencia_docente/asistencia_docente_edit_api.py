from flask_restful import Resource
from app.models import asistencia_docente
from flask import jsonify, request

class Asistencia_docente_edit_api(Resource):
    def get(self):
        return jsonify({"message":"Solo POST"})    

    def post(self):
        data = request.json
        if asistencia_docente.edit_asistencia_docente(data):
            return jsonify({"message":"Actualizado correctamente"})
        return jsonify({"message":"Error al actualizar"}) 
        