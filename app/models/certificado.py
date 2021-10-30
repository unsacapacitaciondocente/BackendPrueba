from .bd_connection import db
import datetime
from .grupo import grupo 
from .curso_capacitacion import curso_capacitacion
from .lista_participante import lista_participante
from .ponente import ponente
from .docente import docente
from .asistencia import asistencia
from .asistencia_docente import asistencia_docente

class certificado(db.Model):
    certificado_id = db.Column(db.Integer,primary_key=True)
    grupo_id = db.Column(db.Integer,nullable=False)
    cer_fecha = db.Column(db.Date,nullable=False)
    cer_disponible_descargas = db.Column(db.Integer,nullable=False)
    cer_user_id = db.Column(db.Integer,nullable=False)
    cer_user_tipo = db.Column(db.String, nullable=False)
    cer_nombre = db.Column(db.String, nullable=False)    

def add_certificado(data):
    try:
        db.session.add(certificado(
            grupo_id=data["grupo_id"],
            cer_fecha=datetime.datetime.strptime(data["fecha"],'%Y-%m-%d'),
            cer_disponible_descargas=data["disponible_descargas"],
            docente_id=data["docente_id"]
            ))
        db.session.commit()           
    except:        
        return False
    return True

def list_certificados_by_user(data):
    # recive {"user_id": 12121212,"tipo":"Administrador"}
    cert = { "lista_certificados":[]}
    list_cert =  certificado.query.filter_by(cer_user_id=data["user_id"],cer_user_tipo=data["tipo"]).all()
    
    for cert in list_cert:
        cert_json = {
        "curso":"",
        "creditos":"",
        "fecha_descarga":"",
        "n_descarga_disponibles":0,
        "estado":""        
        }
        grupo_ = grupo.query.filter_by(grupo_id=data["user_id"]).first()
        #cert_json["curso"] = 

    return cert




    return 1