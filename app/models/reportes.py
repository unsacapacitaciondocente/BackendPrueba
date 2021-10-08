from app.models.grupo import grupo
from app.models.lista_participante import lista_participante
from .bd_connection import db
from .docente import docente
from .curso_capacitacion import curso_capacitacion
from .grupo import grupo

def get_cursos_by_docente(id):
    arr_cursos ={
        "data":[]
    }
    grupos = grupo.query.filter_by(ponente_id=id)
    for gru in  grupos:
        conjunto = {
            "curso":{},
            "grupo":{},
            "docentes":[]
        }
        conjunto["grupo"]= gru.toJSON() # grupo

        curso_cap = curso_capacitacion.query.filter_by(curso_capacitacion_id = gru.curso_capacitacion_id ).first()
        conjunto["curso"] = curso_cap.toJSON()  #curso

        arr_docentes = lista_participante.query.filter_by(grupo_id = gru.grupo_id)

        conjunto_2 = {
            "datos_docente":{},
            "datos_docente_curso":{}
        }
        for doc in arr_docentes:
            conjunto_2["datos_docente_curso"] =  doc.toJSON()
            docente_aux = docente.query.filter_by(docente_id = doc.docente_id)
            conjunto_2["datos_docente"] =  docente_aux.toJSON()
            conjunto["docentes"].append(conjunto_2)  # docentes

        arr_cursos["data"].append(conjunto)
    return arr_cursos