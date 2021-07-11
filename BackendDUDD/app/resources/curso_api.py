from flask_restful import Resource
from app.models import curso
from flask import jsonify

class Curso_api(Resource):
    def get(self):
        
        aux_cursos = curso.get_all_cursos()
        if aux_cursos == None:
            return jsonify({"message":"Ningun curso"})

        return jsonify(curso.get_all_cursos())

    def post(self):
        return jsonify({"message":"Solo GET"})

#edit
#delete
#getid json
#getall json
#postman si o si 