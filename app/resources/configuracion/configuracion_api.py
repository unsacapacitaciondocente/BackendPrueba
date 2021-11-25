from flask_restful import Resource
from app.models import configuracion
from flask import jsonify

class Configuracion_api(Resource):
    def get(self):        
        aux_configuracion = configuracion.get_all_configuracion()
        if aux_configuracion == None:
            return jsonify({"message":"Ningun curso"})
        return jsonify(aux_configuracion)

    def post(self):
        return jsonify({"message":"Solo GET"})
