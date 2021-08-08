from flask_restful import Resource
from app.models import docente
from flask import request, jsonify

class Docente_add_api(Resource):
    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        data = request.json
        if docente.add_docente(data):
            return jsonify({"message":"Registrado correctamente"})
        return jsonify({"message":"Error"})