from flask_restful import Resource
from app.models import ponente
from flask import request, jsonify

class Ponente_add_api(Resource):
    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        data = request.json
        if ponente.add_ponente(data):
            return jsonify({"message":"Registrado correctamente"})
        return jsonify({"message":"Error"})

