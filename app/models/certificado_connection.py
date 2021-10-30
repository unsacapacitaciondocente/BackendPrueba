import cv2 as cv
import os
import app

def get_certificado(data):
    try:
        return 1
    except Exception as e:
        print(e)
        return None

def get_data_certificados(id):
    #INICIO BUSQUEDA EN LA BASE DE DATOS ALL

    #Fin
    contenido = {
        "docente_nombre":"JOSE ALBERTO MAMAMNI GONZALES",
        "docente_calidad":"PARTICIPANTE",
        "docente_aprobado":"APROBADO",
        "docente_nota":"18",
        "curso_contenidos":["Un contenido","Dos contenido","Tres contenido","Cuatro contenido"],
        "curso_nombre":"Matematica",
        "certificado_fecha":"2020-05-12",
        "direccion":"Maria alberta martines",
        "vicerrector":"Edmundo Ramos"
    }
    return contenido
