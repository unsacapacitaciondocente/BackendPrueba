
from flask_restful import Resource
from flask import jsonify, send_file
from tempfile import NamedTemporaryFile
import cv2 as cv
import numpy as np

class Certificado_export(Resource):
    
    def get(self):

        try:
            with NamedTemporaryFile() as temp:
                image_procesed = 255*np.ones((600,1000,3),dtype=np.uint8)

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
                return send_file(iName,mimetype='image/png') 
        except Exception as e:
            return jsonify({"message":str(e)})
        #return jsonify({"message":"Solo POST"})  
        
    def post(self):
        import cv2 as cv
        import numpy as np
        try:
            with NamedTemporaryFile() as temp:
                image_procesed = 255*np.ones((600,1000,3),dtype=np.uint8)

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
                return send_file(iName,mimetype='image/png') 
        except Exception as e:
            return jsonify({"message":str(e)})