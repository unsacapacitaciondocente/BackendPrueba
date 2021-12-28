from flask_restful import Resource
from app.models import asistencia_docente
from flask import request, jsonify

class Asistencia_docente_asistenciaPorFecha(Resource):
    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        data  = request.json
        if asistencia_docente.asistencia_createAsistencia(data):
            return jsonify({"message":"Registrado correctamente"})
        return jsonify({"message":"Error"})
    
class Asistencia_docente_asistenciaListCurso(Resource):
    def get(self,id):
        
        aux_lista_cursos = asistencia_docente.asistencia_lista_cursoDocente(id)
        if aux_lista_cursos == None:
            return jsonify({"message":"Ningun curso"})

        return jsonify(asistencia_docente.asistencia_lista_cursoDocente(id))

    def post(self):
        return jsonify({"message":"Solo GET"})
    
class Asistencia_docente_historialAsistencia(Resource):
    def get(self):
        return jsonify({"message":"Solo post"})

    def post(self):
        data  = request.json
        aux_lista= asistencia_docente.asistencia_historial_docente(data)
        if aux_lista != None:
            return jsonify( asistencia_docente.asistencia_historial_docente(data))
        return jsonify({"message":"Error"})
    
class Asistencia_docente_setAsistencia(Resource):
    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        data  = request.json
        if asistencia_docente.asistencia_setAsistencia(data):
            return jsonify({"message":"Registrado correctamente"})
        return jsonify({"message":"Error"})