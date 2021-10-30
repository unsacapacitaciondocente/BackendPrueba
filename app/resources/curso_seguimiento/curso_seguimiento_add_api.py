from flask_restful import Resource
from app.models import curso_seguimiento
from flask import request, jsonify

class Curso_seguimiento_add_api(Resource):
    def get(self):
        return jsonify({"message":"Solo post"})

    def post(self):
        data  = request.json
        if curso_seguimiento.add_curso_seguimiento(data):
            return jsonify({"message":"Registrado correctamente"})
        return jsonify({"message":"Error"})