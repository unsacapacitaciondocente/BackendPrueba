from flask_restful import Resource
from app.models import curso_seguimiento
from flask import request, jsonify

class Curso_seguimiento_lista_prematriculados(Resource):
    def get(self):
        aux_pre_matriculados = curso_seguimiento.getListaPreMatriculados()
        if aux_pre_matriculados == None:
            return jsonify({"message":"Ningun docente prematriculado"})

        return jsonify(aux_pre_matriculados)
    def post(self):
        return jsonify({"message":"Solo Get"})
    
class Curso_seguimiento_prematriculado(Resource):
    def get(self,id):
        aux_pre_matriculado = curso_seguimiento.getPreMatriculado(id)
        if aux_pre_matriculado == None:
            return jsonify({"message":"Docente No prematriculado"})

        return jsonify(aux_pre_matriculado)
    def post(self):
        return jsonify({"message":"Solo Get"})