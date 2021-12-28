from flask_restful import Resource
from app.models import curso_seguimiento
from flask import request, jsonify

class Curso_seguimiento_detalle_api(Resource):
    
    def get(self, id):
        res = curso_seguimiento.get_curso_seguimiento(id)
        if not res['data']:
            return jsonify({"message":"No existe tal curso"})
        return jsonify(res)
    def post(self):
        return jsonify({"message":"Solo GET"})