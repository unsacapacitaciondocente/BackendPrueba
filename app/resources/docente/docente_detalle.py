from flask_restful import Resource
from app.models import docente
from flask import request, jsonify

class Docente_detalle_api(Resource):    
    def get(self,id):
        return jsonify(docente.detalle_docente(id))
    def post(self):
        return jsonify({"message":"Error"})