from flask_restful import Resource
from app.models import curso
from flask import jsonify, request

class Curso_edit_api(Resource):
    def get(self):
        return jsonify({"message":"Solo POST"})    

    def post(self):
        data = request.json
        if curso.edit_curso(data):
            return jsonify({"message":"Actualizado correctamente"})
        return jsonify({"message":"Error al actualizar"}) 
        