from flask_restful import Resource
from app.models import ponente
from flask import request, jsonify

class Ponente_delete_api(Resource):
    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        key = request.json
        if ponente.delete_ponente(key):
            return jsonify({"message":"Eliminado correctamente"})
        return jsonify({"message":"Error al eliminar"}) 

