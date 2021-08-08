from flask_restful import Resource
from app.models import curso
from flask import jsonify, request

class Curso_delete_api(Resource):
    def get(self):
        return jsonify({"message":"Solo POST"})    

    def post(self):
        key = request.json
        if curso.delete_curso(key):
            return jsonify({"message":"Eliminado correctamente"})
        return jsonify({"message":"Error al eliminar"})   

