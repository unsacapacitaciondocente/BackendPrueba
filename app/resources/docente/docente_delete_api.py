from flask_restful import Resource
from app.models import docente
from flask import request, jsonify

class Docente_delete_api(Resource):    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        key = request.json
        if docente.delete_docente(key):
            return jsonify({"message":"Eliminado correctamente"})
        return jsonify({"message":"Error al eliminar"}) 