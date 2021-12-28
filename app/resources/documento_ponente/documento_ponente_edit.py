
"""
from flask_restful import Resource
from app.models import documento_ponente
from flask import request, jsonify

class Documento_ponente_edit_api(Resource):
    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        data = request.json
        if documento_ponente.edit_documento_ponente(data):
            return jsonify({"message":"Actualizado correctamente"})
        return jsonify({"message":"Error al actualizar"}) 
"""     