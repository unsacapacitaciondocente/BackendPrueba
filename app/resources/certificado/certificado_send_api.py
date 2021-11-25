
from flask_restful import Resource
from flask import jsonify, send_file, url_for
from tempfile import NamedTemporaryFile

import cv2 as cv
import numpy as np
class Certificado_export(Resource):
    
    def get(self):
        return jsonify({"message":"Solo POST"})  
        
    def post(self):
        try:
            data = {
                "contenidos":[
                    "Entorno de PSPP y entorno de SPSS",
                    "Importacion y exportacion de archivos",
                    "Analisis exploratorio de datos",
                    "Pruebas de Hipotesis",
                    "Pruebas de Normalidad",
                    "Pruebas parametricas",
                    "Pruebas no parametricas",
                    "Analisis de varianza",
                    "Analsis de componentes no Principales"
                ],
                "docente":"Otorgado a: ACOSTA GONZALES IRINA XIMENA",
                "cuerpo": 'En calidad de PARTICIPANTE APROBADO (18), durante el curso: \r "METODOS ESTADISTICOS MULTIVARIADOS \r  PARA LA INVESTIGACION USANDO EL PROGRAMA SPSS Y PSPP". Evento que fue realizado por \r la Direccion Universitaria de Desarrollo Docente, del 2 de agosto al 6 de \r  agosto  2021, equivalente a 1 Credito Academico,  \r segun Resolucion Vicerrectoral N° 451-2021-VR.AC.',
                "fecha":"Arequipa, 30 de agosto de 2021",
                "ente1":{
                    "cargo":"DIRECCION UNIVERSITARIA DE DESARROLLO DOCENTE",
                    "nombre":"Dra Nelva Consuelo  Leon de los Santos"
                },
                "ente2":{
                    "cargo":"VICERRECTORADO ACADEMICO",
                    "nombre":"Dra. Ana Maria Guitierrez Valdivia"
                }    
            }

            with NamedTemporaryFile() as temp:
                image_procesed = cv.imread('static/frame1.PNG')

                texto_ = data["docente"]
                ubicacion_ = (320,230)
                font_ = cv.FONT_HERSHEY_PLAIN
                tamañoLetra_ = 1
                colorLetra_ = (0,0,0)
                grosorLetra_ = 1

                cv.putText(image_procesed, texto_, ubicacion_, font_, tamañoLetra_, colorLetra_, grosorLetra_)
                texto_ = data["cuerpo"]
                ubicacion_ = (320,250)
                cv.putText(image_procesed, texto_, ubicacion_, font_, tamañoLetra_, colorLetra_, grosorLetra_)
                iName = "".join([str(temp.name),".PNG"])
                cv.imwrite(iName,image_procesed)
                return send_file(iName,mimetype='image/png')


        except Exception as e:
            return jsonify({"message":str(e)})