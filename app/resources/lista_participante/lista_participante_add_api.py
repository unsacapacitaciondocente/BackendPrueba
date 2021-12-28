from flask_restful import Resource
from app.models import lista_participante
from flask import request, jsonify

class Lista_participante_add_api(Resource):
    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        data  = request.json
        if lista_participante.add_lista_participante(data):
            return jsonify({"message":"Registrado correctamente"})
        return jsonify({"message":"Error"})