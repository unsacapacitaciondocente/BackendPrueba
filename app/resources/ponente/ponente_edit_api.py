from flask_restful import Resource
from app.models import ponente
from flask import request, jsonify

class Ponente_edit_api(Resource):
    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        data = request.json

        if ponente.edit_ponente(data):
            return jsonify({"message":"Actualizado correctamente"})
        return jsonify({"message":"Error al actualizar"}) 

