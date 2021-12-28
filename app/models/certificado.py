from .bd_connection import db
import datetime

class certificado(db.Model):
    certificado_id = db.Column(db.Integer,primary_key=True)
    certificado_nombre = db.Column(db.String,nullable=False)
    certificado_fecha_emision = db.Column(db.Date, nullable=True)
    certificado_cuerpo = db.Column(db.String, nullable=True)
    certificado_descargas = db.Column(db.Integer,nullable=True)
    usuario_id = db.Column(db.Integer,nullable=False)
    usuario_nombre = db.Column(db.String,nullable=False)
    usuario_categoria = db.Column(db.String,nullable=False)
    usuario_estado = db.Column(db.String,nullable=False)
    grupo_id = db.Column(db.Integer,nullable=True)
    curso_contenido = db.Column(db.String,nullable=True)
    curso_nombre = db.Column(db.String,nullable=True)
    curso_creditos = db.Column(db.Integer,nullable=True)
    name_1 = db.Column(db.String,nullable=True)
    name_2 = db.Column(db.String,nullable=True)
    name_3 = db.Column(db.String,nullable=True)
    name_4 = db.Column(db.String,nullable=True)
    name_5 = db.Column(db.String,nullable=True)
    name_6 = db.Column(db.String,nullable=True)
    value_1 = db.Column(db.String,nullable=True)
    value_2 = db.Column(db.String,nullable=True)
    value_3 = db.Column(db.String,nullable=True)
    value_4 = db.Column(db.String,nullable=True)
    value_5 = db.Column(db.String,nullable=True)
    value_6 = db.Column(db.String,nullable=True)
    estado_1 = db.Column(db.Boolean,nullable=True)
    estado_2 = db.Column(db.Boolean,nullable=True)
    estado_3 = db.Column(db.Boolean,nullable=True)
    estado_4 = db.Column(db.Boolean,nullable=True)
    estado_5 = db.Column(db.Boolean,nullable=True)
    estado_6 = db.Column(db.Boolean,nullable=True)
    
    def toJSON(self):
        certificado_json = {
            "certificado_id": self.certificado_id,
            "certificado_nombre":self.certificado_nombre,
            "certificado_fecha_emision":self.certificado_fecha_emision,
            "certificado_cuerpo":self.certificado_cuerpo,
            "certificado_descargas":self.certificado_descargas,            
            "usuario_id":self.usuario_id,
            "usuario_nombre":self.usuario_nombre,
            "usuario_categoria":self.usuario_categoria,
            "usuario_estado":self.usuario_estado,
            "grupo_id":self.grupo_id,
            "curso_nombre":self.curso_nombre,
            "curso_creditos":self.curso_creditos,
            "curso_contenido":self.curso_contenido,
            "nombre_1": self.name_1,
            "nombre_2": self.name_2,
            "nombre_3": self.name_3,
            "nombre_4": self.name_4,
            "nombre_5": self.name_5,
            "nombre_6": self.name_6,
            "valor_1": self.value_1,
            "valor_2": self.value_2,
            "valor_3": self.value_3,
            "valor_4": self.value_4,
            "valor_5": self.value_5,
            "valor_6": self.value_6,
            "estado_1":self.estado_1,
            "estado_2":self.estado_2,
            "estado_3":self.estado_3,
            "estado_4":self.estado_4,
            "estado_5":self.estado_5,
            "estado_6":self.estado_6,
        }
        return certificado_json

def delete_certificado_all(key):
    try:
        certificado_ = certificado.query.filter_by(grupo_id=key["id"])
        db.session.delete(certificado_)
        db.session.commit()
    except:
        return False
    return True

def all_certificados_by_usuario(key):
    arr_certificado ={
        "data":[]
    }
    certificado_ = certificado.query.filter_by(usuario_id=key["usuario_id"],usuario_categoria = key["usuario_categoria"]).all()

    for cert in  certificado_:
        arr_certificado["data"].append(cert.toJSON())
    return arr_certificado

def detalle_certificado(key):
    certificado_detalle = certificado.query.filter_by(certificado_id=key["id"]).first()
    return certificado_detalle.toJSON()
