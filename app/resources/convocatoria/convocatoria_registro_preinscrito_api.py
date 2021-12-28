from flask.wrappers import Request
from flask_restful import Resource
from app.models import convocatoria 
from flask import request, jsonify

class Convocatoria_registro_preinscrito_api(Resource):
    def get(self):
       return jsonify({"message":"Solo post"})

    def post(self):
        registro_preinscrito=request.json
        aux_registro = convocatoria.registro_pre_inscrito(registro_preinscrito)
        if aux_registro == None:
            return jsonify({"message":"No existe el registro"})
        return jsonify(aux_registro)
    