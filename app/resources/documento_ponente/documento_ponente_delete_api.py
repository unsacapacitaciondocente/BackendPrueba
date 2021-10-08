from flask_restful import Resource
from app.models import documento_ponente
from flask import request, jsonify

class Documento_ponente_delete_api(Resource):    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        key = request.json
        if documento_ponente.delete_documento_ponente(key):
            return jsonify({"message":"Eliminado correctamente"})
        return jsonify({"message":"Error al eliminar"}) 