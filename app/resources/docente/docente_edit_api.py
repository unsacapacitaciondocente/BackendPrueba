from flask_restful import Resource
from app.models import docente
from flask import request, jsonify

class Docente_edit_api(Resource):
    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        data = request.json
        if docente.edit_docente(data):
            return jsonify({"message":"Actualizado correctamente"})
        return jsonify({"message":"Error al actualizar"}) 