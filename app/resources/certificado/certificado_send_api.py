
from flask_restful import Resource
from flask import jsonify, send_file
from tempfile import NamedTemporaryFile

class Certificado_export(Resource):
    
    def get(self):
        return jsonify({"message":"Solo POST"})  
        
    def post(self):
        try:
            with NamedTemporaryFile() as temp:
                return jsonify({"message":"holi"}) 
        except Exception as e:
            return jsonify({"message":str(e)})