from flask_restful import Resource
from app.models import configuracion
from flask import request, jsonify

class Configuracion_add_api(Resource):
    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        data  = request.json
        if configuracion.add_configuracion(data):
            return jsonify({"message":"Registrado correctamente"})
        return jsonify({"message":"Error"})
        