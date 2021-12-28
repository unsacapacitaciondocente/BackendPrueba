from .bd_connection import db
from .grupo import grupo
from .curso_capacitacion import curso_capacitacion
from .lista_participante import lista_participante
from .ponente import ponente
from .docente import docente
from .lista_participante import add_lista_participante
import time

# class convocatoria(db.Model):
#   con_id = db.Column(db.Integer,primary_key=True)
#  con_nombre=db.Column(db.String,nullable=False)
#  con_descripcion=db.Column(db.String,nullable=False)
# con_ponente=db.Column(db.String,nullable=False)
# con_hora_inicio=db.Column(db.String,nullable=False)
# con_hora_fin=db.Column(db.String,nullable=False)
# con_estado=db.Column(db.String,nullable=False)

# def toJSON(self):
#    convocatoria_json = {
#            "id": self.con_id,
#            "nombre": self.con_nombre,
#            "descripcion": self.con_descripcion,
#            "ponente": self.con_ponente,
#           "hora_inicio":self.con_hora_inicio,
# "hora_fin": self.con_hora_fin,
#            "estado": self.con_estado
#        }
#       return convocatoria_json

# def get_all_convocatoria():
#    arr_convocatoria ={
#        "data":[]
#    }
#    convocatorias=convocatoria.query.all()
#    for con in  convocatorias:
#        arr_convocatoria["data"].append(con.toJSON())
#    return arr_convocatoria

# here we are


def all_convocatorias():
    convocatorias = {
        "registros": []
    }
    aux_curso_cap = curso_capacitacion.query.filter_by(
        cur_cap_estado="En Convocatoria").all()
    #aux_group = grupo.query.filter_by(gru_estado="En Convocatoria").all()
    for curso in aux_curso_cap:
        grupos = grupo.query.filter_by(
            curso_capacitacion_id=curso.curso_capacitacion_id).all()
        for grupos_aux in grupos:
            convocatoria = {
                "id": id,
                "nombre_curso": "",
                "nombre_grupo": "",
                "descripcion_grupo": "",
                "hora_inicio": "",
                "hora_final": "",
                "fecha_inicio":"",
                "fecha_final":"",
                "horario":"",
            }

            convocatoria["id"] = grupos_aux.grupo_id
            convocatoria["nombre_curso"]= curso.cur_cap_nombre
            convocatoria["nombre_grupo"] = grupos_aux.gru_nombre
            convocatoria["descripcion_grupo"] = curso.cur_cap_descripcion
            convocatoria["hora_inicio"] = grupos_aux.gru_hora_inicio
            convocatoria["hora_final"] = grupos_aux.gru_hora_final
            convocatoria["fecha_inicio"]=curso.cur_cap_fecha_inicial
            convocatoria["fecha_final"]=curso.cur_cap_fecha_final
            convocatoria["horario"]=grupos_aux.gru_horario
            convocatorias["registros"].append(convocatoria)
    return convocatorias["registros"]

def registro_pre_inscrito(data):
    try:
        docente_aux=docente.query.filter_by(docente_id=data["id_docente"]).first()
        pre_registro={
            "grupo_id":data["id_grupo"],
            "docente_id":data["id_docente"],
            "escuela":docente_aux.doc_escuela,
            "departamento":docente_aux.doc_departamento,
            "facultad":docente_aux.doc_facultad,
            "estado":"Inactivo",
            "condicion":"Desaprobado",
            "nota":0,
            "asistencia_actual":0,
            "asistencia_total":0,
            "horas_acumuladas":0
        }
        print(pre_registro)
        add_lista_participante(pre_registro)
    except:
        print("llego hasta aqui!!!!!!!!")
        return False
    return True
    
