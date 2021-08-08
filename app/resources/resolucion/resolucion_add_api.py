from flask_restful import Resource
from app.models import resolucion
from flask import request, jsonify

class Resolucion_add_api(Resource):
    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        data = request.json
        if resolucion.add_resolucion(data):
            return jsonify({"message":"Registrado correctamente"})
        return jsonify({"message":"Error"})
