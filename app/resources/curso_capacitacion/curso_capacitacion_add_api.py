from flask_restful import Resource
from app.models import curso_capacitacion
from flask import request, jsonify

class Curso_capacitacion_add_api(Resource):
    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        data  = request.json
        if curso_capacitacion.add_curso_capacitacion(data):
            return jsonify({"message":"Registrado correctamente"})
        return jsonify({"message":"Error"})
        