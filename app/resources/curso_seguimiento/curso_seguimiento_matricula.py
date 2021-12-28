from flask_restful import Resource
from app.models import curso_seguimiento
from flask import request, jsonify

class Curso_seguimiento_matricular(Resource):
    def get(self):
        return jsonify({"message":"Solo POST"}) 

    def post(self):
        data = request.json

        if curso_seguimiento.matricularDocente(data):
            return jsonify({"message":"Se matriculo docente exitosamente!"})
        return jsonify({"message":"No se pudo matricular docente"}) 

class Curso_seguimiento_desmatricular(Resource):
    def get(self):
        return jsonify({"message":"Solo POST"}) 

    def post(self):
        data = request.json

        if curso_seguimiento.desmatricularDocente(data):
            return jsonify({"message":"Se desmatriculo docente exitosamente!"})
        return jsonify({"message":"No se pudo desmatricular docente"})

class Curso_seguimiento_prematricular(Resource):
    def get(self):
        return jsonify({"message":"Solo POST"}) 

    def post(self):
        data = request.json

        if curso_seguimiento.preMatricularDocente(data):
            return jsonify({"message":"Se pre-matriculo exitosamente!"})
        return jsonify({"message":"No se pudo pre-matricular"}) 

class Curso_seguimiento_cambio_estado(Resource):
    def get(self):
        return jsonify({"message":"Solo POST"}) 

    def post(self):
        data = request.json

        if curso_seguimiento.cambiarEstado(data):
            return jsonify({"message":"Se cambió el estado"})
        return jsonify({"message":"No se pudo cambiar el estado"}) 
