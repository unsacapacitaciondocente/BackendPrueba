
from flask_restful import Resource
from app.models import curso
from flask import request, jsonify, send_file,send_from_directory,Response
from tempfile import NamedTemporaryFile
import os
from app import app
from app.models import certificado_connection
import cv2 as cv
import numpy as np

class Certificado_export(Resource):
    
    def get(self):
        return jsonify({"message":"Solo POST"})  
        
    def post(self):
        try:
            data = request.json
            datos =certificado_connection.get_data_certificados(data["id"])
            with NamedTemporaryFile() as temp:
                image_procesed = cv.imread('c_1.PNG')
                #image_procesed = 255*np.ones((600,1000,3),dtype=np.uint8)

                texto_ = "nombre"
                ubicacion_ = (5,50)
                font_ = cv.FONT_HERSHEY_PLAIN
                tamañoLetra_ = 1
                colorLetra_ = (0,0,0)
                grosorLetra_ = 1

                cv.putText(image_procesed, texto_, ubicacion_, font_, tamañoLetra_, colorLetra_, grosorLetra_)
                texto_ = "something else"
                ubicacion_ = (5,70)
                cv.putText(image_procesed, texto_, ubicacion_, font_, tamañoLetra_, colorLetra_, grosorLetra_)
 

                iName = "".join([str(temp.name),".PNG"])
                cv.imwrite(iName,image_procesed)
                #cv.imwrite(str(temp.name), image_procesed)
                return send_file(iName,mimetype='image/png') 
        except Exception as e:
            return jsonify({"message":str(e)})