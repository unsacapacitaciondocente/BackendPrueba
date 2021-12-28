from .certificado import certificado
from .grupo import grupo 
from .curso_capacitacion import curso_capacitacion
from .lista_participante import lista_participante
from .docente import docente
from .ponente import ponente
import datetime
from .bd_connection import db
from .configuracion import configuracion

def generate_certificados_docentes(key):
    
    lista_participante_aux = lista_participante.query.filter_by( grupo_id = key["gru_id"],lis_par_condicion ="Aprobado" ).all()
    grupo_aux = grupo.query.filter_by(grupo_id = key["gru_id"]).first()
    curso_capacitacion_aux = curso_capacitacion.query.filter_by(curso_capacitacion_id = grupo_aux.curso_capacitacion_id).first()
    configuracion_= configuracion.query.filter_by(configuracion_id=1).first()
    configuracion_2= configuracion.query.filter_by(configuracion_id=2).first()
    try:
        for participante in lista_participante_aux:

            docente_aux = docente.query.filter_by(docente_id = participante.docente_id).first()

            #variables
            certificado_nombre_ ="" #resolved
            certificado_fecha_emision_ =datetime.datetime.now() #resolved
            usuario_id_ = participante.docente_id #resolved
            usuario_nombre_ = "Otorgado a: "+ docente_aux.doc_nombre.upper() #resolved
            usuario_categoria_ = "Docente" #resolved
            usuario_estado_ = participante.lis_par_condicion #resolved
            grupo_id_  = participante.grupo_id #resolved
            curso_contenidos_ = ""#resolved --
            curso_nombre_  = "" # resolved --
            curso_creditos_  ="" # resolved --
            #busqueda

            curso_creditos_  = curso_capacitacion_aux.cur_cap_creditaje
            curso_nombre_ = curso_capacitacion_aux.cur_cap_nombre
            curso_contenidos_ = curso_capacitacion_aux.cur_cap_descripcion
            if len(curso_nombre_)>10:
                certificado_nombre_ = "DUDD -"+curso_nombre_[:9]+"-"+grupo_aux.gru_nombre+"-"+usuario_categoria_[0:3]+"-"+str(usuario_id_)
            else:
                certificado_nombre_ = "DUDD -"+curso_nombre_+"-"+grupo_aux.gru_nombre+"-"+usuario_categoria_[0:3]+"-"+str(usuario_id_)

            certificado_cuerpo_ = "En calidad de PARTICIPANTE APROBADO ("+ str(participante.lis_nota)  +'), durante el curso: "'+  curso_nombre_.upper() + '". Evento que fue realizado por la Direccion Universitaria  de Desarrollo Docente, del '+ curso_capacitacion_aux.cur_cap_fecha_inicial + " al "+ curso_capacitacion_aux.cur_cap_fecha_final + ", equivalente a "+str(curso_creditos_) + " Creditos Academicos, segun "+ curso_capacitacion_aux.cur_cap_resolucion 

            db.session.add(certificado(
                certificado_nombre = certificado_nombre_, 
                certificado_fecha_emision = certificado_fecha_emision_, 
                certificado_cuerpo = certificado_cuerpo_,  
                usuario_id = usuario_id_, 
                usuario_nombre = usuario_nombre_, 
                usuario_categoria = usuario_categoria_, 
                usuario_estado = usuario_estado_, 
                grupo_id = grupo_id_, 
                curso_contenido = curso_contenidos_, 
                curso_nombre = curso_nombre_, 
                curso_creditos = curso_creditos_, 
                certificado_descargas = 0,
                name_1 = configuracion_.name_1 ,
                name_2 = configuracion_.name_2 ,
                name_3 = configuracion_.name_3 ,
                name_4 = configuracion_.name_4,
                name_5 = configuracion_.name_5 ,
                name_6 = configuracion_.name_6 ,
                value_1 = configuracion_.value_1 ,
                value_2 = configuracion_.value_2,
                value_3 = configuracion_.value_3,
                value_4 = configuracion_.value_4,
                value_5 = configuracion_.value_5,
                value_6 = configuracion_.value_6,
                estado_1 = configuracion_.estado_1,
                estado_2 = configuracion_.estado_2,
                estado_3 = configuracion_.estado_3,
                estado_4 = configuracion_.estado_4,
                estado_5 = configuracion_.estado_5,
                estado_6 = configuracion_.estado_6
                ) )
            db.session.commit()      
        #ponente
        ponente_ = ponente.query.filter_by(ponente_id = key["pon_id"]).first()
        #variables
        if (ponente_ != None):
            certificado_nombre_ ="" #resolved
            certificado_fecha_emision_ =datetime.datetime.now() #resolved
            usuario_id_ = ponente_.ponente_id #resolved
            usuario_nombre_ = "Otorgado a: "+ ponente_.pon_nombre.upper() #resolved
            usuario_categoria_ = "Ponente" #resolved
            usuario_estado_ = ""#resolved
            grupo_id_  = key["gru_id"] #resolved
            curso_contenidos_ = ""#resolved --
            curso_nombre_  = "" # resolved --
            curso_creditos_  ="" # resolved --
            #busqueda

            curso_creditos_  = curso_capacitacion_aux.cur_cap_creditaje
            curso_nombre_ = curso_capacitacion_aux.cur_cap_nombre
            curso_contenidos_ = curso_capacitacion_aux.cur_cap_descripcion
            if len(curso_nombre_)>10:
                certificado_nombre_ = "DUDD -"+curso_nombre_[:9]+"-"+grupo_aux.gru_nombre+"-"+usuario_categoria_[0:3]+"-"+str(usuario_id_)
            else:
                certificado_nombre_ = "DUDD -"+curso_nombre_+"-"+grupo_aux.gru_nombre+"-"+usuario_categoria_[0:3]+"-"+str(usuario_id_)

            certificado_cuerpo_ = "En calidad de PONENTE del curso:"+ '"'+  curso_nombre_.upper() + '". Evento que fue realizado por la Direccion Universitaria  de Desarrollo Docente, del '+ curso_capacitacion_aux.cur_cap_fecha_inicial + " al "+ curso_capacitacion_aux.cur_cap_fecha_final + ", equivalente a "+str(curso_creditos_) + " Creditos Academicos, segun "+ curso_capacitacion_aux.cur_cap_resolucion 

            db.session.add(certificado(
                certificado_nombre = certificado_nombre_, 
                certificado_fecha_emision = certificado_fecha_emision_, 
                certificado_cuerpo = certificado_cuerpo_,  
                usuario_id = usuario_id_, 
                usuario_nombre = usuario_nombre_, 
                usuario_categoria = usuario_categoria_, 
                usuario_estado = usuario_estado_, 
                grupo_id = grupo_id_, 
                curso_contenido = curso_contenidos_, 
                curso_nombre = curso_nombre_, 
                curso_creditos = curso_creditos_, 
                certificado_descargas = 0,
                name_1 = configuracion_2.name_1 ,
                name_2 = configuracion_2.name_2 ,
                name_3 = configuracion_2.name_3 ,
                name_4 = configuracion_2.name_4,
                name_5 = configuracion_2.name_5 ,
                name_6 = configuracion_2.name_6 ,
                value_1 = configuracion_2.value_1 ,
                value_2 = configuracion_2.value_2,
                value_3 = configuracion_2.value_3,
                value_4 = configuracion_2.value_4,
                value_5 = configuracion_2.value_5,
                value_6 = configuracion_2.value_6,
                estado_1 = configuracion_2.estado_1,
                estado_2 = configuracion_2.estado_2,
                estado_3 = configuracion_2.estado_3,
                estado_4 = configuracion_2.estado_4,
                estado_5 = configuracion_2.estado_5,
                estado_6 = configuracion_2.estado_6
                ) )
            db.session.commit() 

        return True
    except Exception as e:
        print(repr(e))
        return False 

def deleteCertificatesByDocente(key):
    try:
        certificado.query.filter_by(grupo_id=key["gru_id"]).delete()
        db.session.commit()
        return True
    except Exception as e:
        print(repr(e))
        return False

def incrementDowload(id):
    try: 
        cert_ = certificado.query.filter_by(certificado_id=id).first()
        cert_.certificado_descargas = cert_.certificado_descargas+1
        db.session.commit()
        return True
    except Exception as e:
        print(repr(e))
        return False









        

