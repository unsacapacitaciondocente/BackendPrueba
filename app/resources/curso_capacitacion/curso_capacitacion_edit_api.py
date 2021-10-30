from flask_restful import Resource
from app.models import curso_capacitacion
from flask import jsonify, request

class Curso_capacitacion_edit_api(Resource):
    def get(self):
        return jsonify({"message":"Solo POST"})    

    def post(self):
        data = request.json
        if curso_capacitacion.edit_curso_capacitacion(data):
            return jsonify({"message":"Actualizado correctamente"})
        return jsonify({"message":"Error al actualizar"}) 
        