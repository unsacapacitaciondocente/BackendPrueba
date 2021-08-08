from flask_restful import Resource
from app.models import resolucion
from flask import request, jsonify

class Resolucion_delete_api(Resource):
    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        key = request.json
        if resolucion.delete_resolucion(key):
            return jsonify({"message":"Eliminado correctamente"})
        return jsonify({"message":"Error al eliminar"}) 
