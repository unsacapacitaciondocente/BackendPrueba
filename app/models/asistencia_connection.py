from .bd_connection import db
from .grupo import grupo 
from .curso_capacitacion import curso_capacitacion
from .lista_participante import lista_participante
from .ponente import ponente
from .docente import docente
from .asistencia import asistencia
from .asistencia_docente import asistencia_docente
from .asistencia import add_asistencia
from .asistencia_docente import add_asistencia_docente,asistencia_setAsistencia,asistencia_createAsistencia
import time
from datetime import datetime, timedelta
from .tiempo import generar_fecha_actual

def group_for_assistance(id):
    group_for_assistance = {
        "nombre_curso": "",
        "descripcion_curso":"",
        "total_asistencia":0,
        "lista participantes":[]
    }

    grupo_aux = grupo.query.filter_by(grupo_id = id ).first()
    curso_aux = curso_capacitacion.query.filter_by(curso_capacitacion_id = grupo_aux.curso_capacitacion_id ).first()

    group_for_assistance["nombre_curso"]= curso_aux.cur_cap_nombre
    group_for_assistance["descripcion_curso"]= curso_aux.cur_cap_descripcion
    group_for_assistance["total_asistencia"]= curso_aux.cur_cap_total_asistencia #no esta en la BD

    lista_participante_aux = lista_participante.query.filter_by( grupo_id =id)

    for participante in lista_participante_aux :
        participante_aux = {
            "docente_id":123123,
            "nombre_participante": "",
            "estado":"",
            "nota_final":0.1,
            "numero_asistencias":12
        }
        
        participante_aux["estado"] = participante.lis_par_estado
        participante_aux["nota_final"] = participante.lis_nota
        participante_aux["numero_asistencias"] = participante.lis_par_asistencia_total
        participante_aux["docente_id"] = participante.docente_id

        docente_aux = docente.query.filter_by(docente_id = participante.docente_id ).first()

        participante_aux["nombre_participante"] = docente_aux.doc_nombre
        group_for_assistance["lista participantes"].append(participante_aux)

    return group_for_assistance

def lista_cursos_ponente(id):
    lista_cursos_ponente = {
        "list_course":[]
    }
    aux_group_array= grupo.query.filter_by(ponente_id= id).all()
    for aux_group in aux_group_array:

        aux_course_json = {
        "id":aux_group.grupo_id,
        "nombre":"",
        "cantidad_asistentes":0
        }

        aux_course=curso_capacitacion.query.filter_by(curso_capacitacion_id = aux_group.curso_capacitacion_id).first()
        if aux_course !=None:
            aux_course_json["nombre"]=aux_course.cur_cap_nombre+(" - Grupo: ")+aux_group.gru_nombre
            aux_docente_list=lista_participante.query.filter_by(grupo_id=aux_group.grupo_id).all()
            aux_course_json["cantidad_asistentes"]=len(aux_docente_list)
            lista_cursos_ponente["list_course"].append(aux_course_json)

    return lista_cursos_ponente

## Metodo solicitar todos los docentes para marcar asistencia masiva, tambien crear asistencia.
def registro_asistencias(id):
    #Primero se creara un array con todos los docentes del grupo
    registro={
        "id":id,
        "nombre_curso":"",
        "fecha":"",
        "comentario":"",
        "asistentes":0,
        "asistencias":[]
    }
    
    aux_group = grupo.query.filter_by(grupo_id = id).first()
    aux_course=curso_capacitacion.query.filter_by(curso_capacitacion_id= aux_group.curso_capacitacion_id).first() 
    registro["nombre_curso"] = aux_group.gru_nombre + " / " + aux_course.cur_cap_nombre
       
    aux_lista_asistentes=lista_participante.query.filter_by(grupo_id = id).all()
    for asistente in aux_lista_asistentes:
        aux_asistente = {
            "id":0,
            "nombre":"",
            "correo":"",
            "asistencia":False
        }
        aux_docente =  docente.query.filter_by(docente_id= asistente.docente_id).first()
        aux_asistente["id"]=aux_docente.docente_id
        aux_asistente["nombre"]= aux_docente.doc_nombre
        aux_asistente["correo"]= aux_docente.doc_email
        registro["asistencias"].append(aux_asistente)
        
    #Aqui se empieza a crear la nueva asistencia con la fecha de hoidia
    asistencia_nueva = {
            "date_now": generar_fecha_actual(),
            "id_grupo": id,
            "descripcion_estado": "No hay comentarios",
            "estado": "Activo"
        }
    
    asistencia_createAsistencia(asistencia_nueva)
   
    return registro

def guardar_registro_asistencia(data):
    asistencia_aux=asistencia.query.filter_by(asi_fecha=data["fecha"]).first()
    for asistentes in data["asistencias"]:
        if asistentes["asistencia"]=="Asistio":
            asistencia_docente_nueva = {
                "date_now": data["fecha"],
                "asistencia_id": asistencia_aux.asistencia_id,
                "descripcion_estado": data["comentario"],
                "estado": asistentes["asistencia"],
                "id_docente": asistentes["id"],
                "id_grupo":data["id"]
            }
            asistencia_setAsistencia(asistencia_docente_nueva)
      
        
    
def historial_asistencias(id):
    historial = {
        "id":id,
        "nombre_curso":"",
        "asistencias":[]        
    }
    aux_group = grupo.query.filter_by(grupo_id =id).first()

    if (aux_group != None):
        aux_course=curso_capacitacion.query.filter_by(curso_capacitacion_id= aux_group.curso_capacitacion_id).first() 
        historial["nombre_curso"] = aux_group.gru_nombre + " / " + aux_course.cur_cap_nombre


        aux_asistencia = asistencia.query.filter_by(grupo_id = id ).all()
        for asist in aux_asistencia:
            asist_json = {
                "id":0,
                "fecha":"",
                "asistentes":0,
                "comentarios":""
            }
            asist_json["id"]=asist.asistencia_id
            asist_json["fecha"]=asist.asi_fecha.strftime("%Y-%m-%d")
            asist_json["comentarios"] = asist.asi_comentario
            
            aux_list_asistencia_docente =  asistencia_docente.query.filter_by(asistencia_id= asist.asistencia_id ).all()
            asist_json["asistentes"]=len(aux_list_asistencia_docente)

            historial["asistencias"].append(asist_json)
    return historial

def calificaciones_docente(id):
    calificaciones={
        "id":id,
        "nombre_curso":"",
        "descripcion":"",
        "total_asistencias":0,
        "docentes":[]
    }

    aux_group=grupo.query.filter_by(grupo_id=id).first()

    if aux_group !=None:
       aux_docente=curso_capacitacion.query.filter_by(curso_capacitacion_id=aux_group.curso_capacitacion_id).first()
       #nombre del curso
       calificaciones["nombre_curso"]=aux_docente.cur_cap_nombre  + " / Grupo: " + aux_group.gru_nombre
       #descripcion
       calificaciones["descripcion"]=aux_docente.cur_cap_descripcion
       #total_Asistencias
       aux_asistencias=asistencia.query.filter_by(grupo_id=id).all()
       calificaciones["total_asistencias"]=len(aux_asistencias)

        
       #docentes
       lista_docente_aux=lista_participante.query.filter_by(grupo_id=id).all()

       for docente_ in lista_docente_aux:
           docente_aux={
               "docente_id":0,
               "nombre_docente":"",
               "estado_docente":"",
               "nota_final_docente":0.1,
               "horas_docente":0,
               "numero_asistencias":0,
               
           }
           #id
           docente_aux["docente_id"]=docente_.docente_id
           #nombre
           docente_nombre=docente.query.filter_by(docente_id=docente_.docente_id).first()
           if docente_nombre != None: 
                docente_aux["nombre_docente"]=docente_nombre.doc_nombre
            #estado
                docente_aux["estado_docente"]=docente_.lis_par_condicion
            #nota 
                docente_aux["nota_final_docente"]=docente_.lis_nota
             #horas 
                docente_aux["horas_docente"]=docente_.lis_par_horas_acumuladas
            #numero de asistencias
                if docente_.lis_par_asistencia_total==0:
                    docente_aux["numero_asistencias"]=0
                else:
                    docente_aux["numero_asistencias"]=docente_.lis_par_asistencia_actual/docente_.lis_par_asistencia_total

                calificaciones["docentes"].append(docente_aux)
                

    return calificaciones


def edit_calificacion(calificaciones):
    try:
        #participantes= lista_participante.query.filter_by(grupo_id=calificaciones['id']).all()
        for participante in calificaciones['docentes']:
          docente_aux=lista_participante.query.filter_by(docente_id=participante['docente_id']).first()
        #estado
          docente_aux.lis_par_condicion=participante["estado_docente"]
        #nota final docente    
          docente_aux.lis_nota=participante["nota_final_docente"]
          db.session.commit()
    except:
        return False
    return True


def edit_asistencia(crear_asistencia): 
    try:
        nueva_asistencia = {
            "fecha": crear_asistencia['fecha'],
            "grupo_id": crear_asistencia['id'],
            "comentario": crear_asistencia['comentario'],
            "estado": True, 
        }
        add_asistencia(nueva_asistencia)
        time.sleep(2)
        asistencia_agregada=asistencia.query.filter_by(asi_fecha=crear_asistencia['fecha']).first()
        id_asistencia=asistencia_agregada['asistencia_id']
        print(id_asistencia)
        
        for asistente in crear_asistencia['asistencias']:
            nueva_asistencia_docente = {
            "fecha": crear_asistencia['fecha'] ,
            "asistencia_id": id_asistencia ,
            "comentario": crear_asistencia['comentario'],
            "estado": True, 
            "docente_id": asistente['id'],
            }
            add_asistencia_docente(nueva_asistencia_docente)
        
           
    except:
        return False
    return True






        