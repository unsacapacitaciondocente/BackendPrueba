from flask_restful import Resource
from app.models import curso_seguimiento
from flask import request, jsonify

class Curso_seguimiento_cursos(Resource):
    def get(self):
        return jsonify({"message":"Solo POST"}) 

    def post(self):
        data = request.json
        result = curso_seguimiento.getCursosPorEstado(data)
        if result == None:
            return jsonify({"message":"Ningun curso en ese estado"})

        return jsonify(result)

class Curso_seguimiento_ponentes(Resource):
    def get(self):
        result = curso_seguimiento.getPonentesActivos()
        if result == None:
            return jsonify({"message":"Ningun ponente activo"})

        return jsonify(result)

    def post(self):
        return jsonify({"message":"Solo GET"}) 