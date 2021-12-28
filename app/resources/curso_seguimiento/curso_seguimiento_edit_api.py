from flask_restful import Resource
from app.models import curso_seguimiento
from flask import jsonify, request

class Curso_seguimiento_edit_api(Resource):
    def get(self):
        return jsonify({"message":"Solo POST"})    

    def post(self):
        data = request.json
        if curso_seguimiento.edit_curso_seguimiento(data):
            return jsonify({"message":"Actualizado correctamente"})
        return jsonify({"message":"Error al actualizar"}) 