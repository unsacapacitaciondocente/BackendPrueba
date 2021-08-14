from flask_restful import Resource
from app.models import usuario
from flask import request, jsonify

class Usuario_detalle_api(Resource):    
    def get(self,id):
        return jsonify(usuario.detalle_docente(id))
    def post(self):
        return jsonify({"message":"Error"})