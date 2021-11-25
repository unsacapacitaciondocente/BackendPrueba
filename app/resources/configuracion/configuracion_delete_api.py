from flask_restful import Resource
from app.models import configuracion
from flask import jsonify, request

class Configuracion_delete_api(Resource):
    def get(self):
        return jsonify({"message":"Solo POST"})    

    def post(self):
        key = request.json
        if configuracion.delete_configuracion(key):
            return jsonify({"message":"Eliminado correctamente"})
        return jsonify({"message":"Error al eliminar"})   