from .bd_connection import db
from .asistencia import add_asistencia
from .lista_participante import edit_lista_participante
from .asistencia import asistencia
from .lista_participante import lista_participante
from .curso_capacitacion import curso_capacitacion
from .grupo import grupo
from .ponente import ponente
from datetime import datetime, timedelta
from .tiempo import generar_fecha_actual

class asistencia_docente(db.Model):
    asistencia_day_id = db.Column(db.Integer,primary_key=True)
    asi_doc_fecha = db.Column(db.Date,nullable=False)
    asistencia_id = db.Column(db.Integer,nullable=False)
    asi_doc_comentario = db.Column(db.String,nullable=False)
    asi_doc_estado = db.Column(db.String,nullable=False)
    docente_id = db.Column(db.Integer,nullable=False)

    def toJSON(self):
        asistencia_docente_json = {
            "id": self.asistencia_day_id,
            "fecha": self.asi_doc_fecha.strftime("%Y-%m-%d"),
            "asistencia_id": self.asistencia_id,
            "comentario": self.asi_doc_comentario,
            "estado": self.asi_doc_estado,
            "docente_id": self.docente_id 
        }
        return asistencia_docente_json

 
def add_asistencia_docente(data):
    try:

        db.session.add(asistencia_docente(asi_doc_fecha=data["fecha"],asistencia_id=data["asistencia_id"],asi_doc_comentario=data["comentario"],asi_doc_estado=data["estado"],docente_id=data["docente_id"]))
        db.session.commit()  
 
                 
    except:
        return False
    return True

def get_all_asistencia_docente():
    arr_asistencia_docente ={
        "data":[]
    }
    asistencia_docentes = asistencia_docente.query.all()
    for cur in  asistencia_docentes:
        arr_asistencia_docente["data"].append(cur.toJSON())
    return arr_asistencia_docente

def edit_asistencia_docente(data):
    try:
        asistencia_docente_ = asistencia_docente.query.filter_by(asistencia_docente_id=data["id"]).first()
        asistencia_docente_.asi_doc_fecha=data["fecha"]
        asistencia_docente_.asistencia_id=data["grupo_id"]
        asistencia_docente_.asi_doc_comentario=data["comentario"]
        asistencia_docente_.asi_doc_estado=data["estado"]
        asistencia_docente_.docente_id=data["docente_id"]
        
        db.session.commit()
    except:
        return False
    return True

def delete_asistencia_docente(key):
    try:
        asistencia_docente_ = asistencia_docente.query.filter_by(asistencia_docente_id=key["id"]).first()
        db.session.delete(asistencia_docente_)
        db.session.commit()
    except:
        return False
    return True

def detalle_asistencia_docente(id):
    
    asistencia_docente_ = asistencia_docente.query.filter_by(asistencia_docente_id=id).first()

    if asistencia_docente_ == None:
        return {"message":"No se ha podido obtener"}
    return asistencia_docente_.toJSON()


def asistencia_createAsistencia(data):
    crear_asistencia = {
        "fecha": data['date_now'],
        "grupo_id": data['id_grupo'],
        "comentario": data['descripcion_estado'],
        "estado": data['estado']
    }
    
    lista_participante_aux=lista_participante.query.filter_by(grupo_id=data['id_grupo']).all()
    try:
        for participante in lista_participante_aux:
            participante.lis_par_asistencia_total= participante.lis_par_asistencia_total +1
            
        add_asistencia(crear_asistencia)
        print("se agrego la asistencia")          
    except:
        return False
    return True
    
def asistencia_lista_cursoDocente(id):
    lista_cursoDocente = {
        "lista_coursos":[]
    }
    aux_list = lista_participante.query.filter_by(docente_id = id).all()
    for curso in aux_list:
        aux_curso_docente = {
        "id_grupo":0,
        "nombre_curso":"",
        "nombre_grupo":"",
        "horario":"",
        "nombre_ponente":"",
        "id_teacher":int(id)
        }
        aux_curso_docente["id_grupo"]=curso.grupo_id
        encontrar_grupo= grupo.query.filter_by(grupo_id=curso.grupo_id).first()
        encontrar_curso= curso_capacitacion.query.filter_by(curso_capacitacion_id=encontrar_grupo.curso_capacitacion_id).first()
        aux_curso_docente["nombre_curso"]=encontrar_curso.cur_cap_nombre
        aux_curso_docente["nombre_grupo"]=encontrar_grupo.gru_nombre
        aux_curso_docente["horario"]=encontrar_grupo.gru_horario
        encontrar_ponente=ponente.query.filter_by(ponente_id=encontrar_grupo.ponente_id).first()
        aux_curso_docente["nombre_ponente"]=encontrar_ponente.pon_nombre
        lista_cursoDocente["lista_coursos"].append(aux_curso_docente)
    return lista_cursoDocente["lista_coursos"]

def asistencia_historial_docente(data):
    datos={
        "id_grupo":data["id_grupo"],
        "nombre_curso":"",
        "nombre_grupo":"",
        "date_now":"",
        "asistencias_Docente":[]
    }
    encontrar_grupo=grupo.query.filter_by(grupo_id=data["id_grupo"]).first()
    encontrar_curso=curso_capacitacion.query.filter_by(curso_capacitacion_id=encontrar_grupo.curso_capacitacion_id).first()
    datos["nombre_curso"]=encontrar_curso.cur_cap_nombre
    datos["nombre_grupo"]=encontrar_grupo.gru_nombre
    datos["date_now"]=generar_fecha_actual()
    asistencias_tomadas=asistencia.query.filter_by(grupo_id=data["id_grupo"]).all()
    for asistencia_tomada in asistencias_tomadas:
        registro_asistencia={
            "id":0,
            "fecha":"",
            "estado":"",
            "descripcion_estado":"",
            "id_grupo":0,
            "id_docente":0,
            "date_now":"",
            "id_ponente_creador":0
        }
        registro_asistencia["id"]=asistencia_tomada.asistencia_id
        
        registro_asistencia["fecha"]=asistencia_tomada.asi_fecha.strftime('%Y-%m-%d')
    
        encontrar_asistencia=asistencia_docente.query.filter_by(asistencia_id=asistencia_tomada.asistencia_id,docente_id=data["id_teacher"]).first()
        if encontrar_asistencia==None:
            registro_asistencia["estado"]="No asistio"
        else:
            registro_asistencia["estado"]="Asistio"
        registro_asistencia["descripcion_estado"]="No hay comentarios"
        registro_asistencia["id_grupo"]=data["id_grupo"]
        registro_asistencia["id_docente"]=data["id_teacher"]
        registro_asistencia["date_now"]=generar_fecha_actual()
        registro_asistencia["id_ponente_creador"]=encontrar_grupo.ponente_id
        datos["asistencias_Docente"].append(registro_asistencia)
    return datos
        
def asistencia_setAsistencia(data):
    encontrar_asistenciaHoidia=asistencia.query.filter_by(grupo_id=data["id_grupo"] ,asi_fecha=data["date_now"]).first()
    cargar_asistenciaDocente = {
            "fecha": data["date_now"],
            "asistencia_id": encontrar_asistenciaHoidia.asistencia_id,
            "comentario": data["descripcion_estado"],
            "estado": data["estado"],
            "docente_id":  data["id_docente"]
        }
    grupo_aux=grupo.query.filter_by(grupo_id=data["id_grupo"]).first()
    format = '%H:%M'
    time=datetime.strptime(grupo_aux.gru_hora_final,format) - datetime.strptime(grupo_aux.gru_hora_inicio,format)
    horas=time/timedelta(hours=1)
    participante = lista_participante.query.filter_by(docente_id = data["id_docente"],grupo_id=data["id_grupo"]).first()
    try:
        participante.lis_par_horas_acumuladas= participante.lis_par_horas_acumuladas + horas
        participante.lis_par_asistencia_actual=participante.lis_par_asistencia_actual+1
        edit_lista_participante(participante)
        add_asistencia_docente(cargar_asistenciaDocente)
    except:
        return False
    return True