from flask_restful import Resource
from app.models import configuracion
from flask import jsonify, request

class Configuracion_edit_api(Resource):
    def get(self):
        return jsonify({"message":"Solo POST"})    

    def post(self):
        data = request.json
        if configuracion.edit_configuracion(data):
            return jsonify({"message":"Actualizado correctamente"})
        return jsonify({"message":"Error al actualizar"}) 
        