from flask_restful import Resource
from app.models import correo 
from flask import request, jsonify

class Correo_convocatoria_api(Resource):
    
    def get(self):
        return jsonify({"message":"Solo post"})
    def post(self):
        data = request.json
        return jsonify({"message":correo.send_email(data)})