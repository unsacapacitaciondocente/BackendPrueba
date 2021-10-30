from flask_restful import Resource
from app.models import curso_capacitacion
from flask import jsonify

class Curso_capacitacion_api(Resource):
    def get(self):
        
        aux_cursos_capacitacion = curso_capacitacion.get_all_curso_capacitacion()
        if aux_cursos_capacitacion	 == None:
            return jsonify({"message":"Ningun curso"})

        return jsonify(curso_capacitacion.get_all_curso_capacitacion())

    def post(self):
        return jsonify({"message":"Solo GET"})
