from flask_restful import Resource
from app.models import grupo
from flask import request, jsonify

class Grupo_detalle_api(Resource):    
    def get(self,id):
        return jsonify(grupo.detalle_grupo(id))
    def post(self):
        return jsonify({"message":"Error"})