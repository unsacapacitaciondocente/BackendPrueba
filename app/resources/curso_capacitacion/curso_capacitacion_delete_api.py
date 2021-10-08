from flask_restful import Resource
from app.models import curso_capacitacion
from flask import jsonify, request

class Curso_capacitacion_delete_api(Resource):
    def get(self):
        return jsonify({"message":"Solo POST"})    
 
    def post(self):
        key = request.json
        if curso_capacitacion.delete_curso_capacitacion(key):
            return jsonify({"message":"Eliminado correctamente"})
        return jsonify({"message":"Error al eliminar"})   

