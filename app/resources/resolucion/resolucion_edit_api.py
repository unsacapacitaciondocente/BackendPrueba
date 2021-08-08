from flask_restful import Resource
from app.models import resolucion
from flask import request, jsonify

class Resolucion_edit_api(Resource):
    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        data = request.json

        if resolucion.edit_resolucion(data):
            return jsonify({"message":"Actualizado correctamente"})
        return jsonify({"message":"Error al actualizar"}) 
