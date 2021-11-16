from .bd_connection import db
import datetime

class certificado(db.Model):
    certificado_id = db.Column(db.Integer,primary_key=True)
    certificado_nombre = db.Column(db.String,nullable=False)
    certificado_fecha_emision = db.Column(db.Date, nullable=True)
    usuario_id = db.Column(db.Integer,nullable=False)
    usuario_categoria = db.Column(db.String,nullable=False)
    usuario_nombre = db.Column(db.String,nullable=True)
    usuario_estado = db.Column(db.String,nullable=False)
    usuario_nota = db.Column(db.Float, nullable=True)
    grupo_id = db.Column(db.Integer,nullable=True)
    curso_contenido = db.Column(db.String,nullable=True)
    curso_nombre = db.Column(db.String,nullable=True)
    curso_fecha_inicio = db.Column(db.Date,nullable=True)
    curso_fecha_fin = db.Column(db.Date,nullable=True)    
    curso_resolucion = db.Column(db.String,nullable=True)
    curso_creditaje = db.Column(db.Float,nullable=True)
    certificado_descargas = db.Column(db.Integer,nullable=True)
    
    def toJSON(self):
        certificado_json = {
            "id": self.certificado_id,
            "fecha":self.certificado_fecha_emision.strftime("%Y-%m-%d"),
            "descargas":self.certificado_descargas,
            "curso":self.curso_nombre,
            "creditos":self.curso_creditaje,
            "estado":self.usuario_estado
        }
        return certificado_json
    def toJsonUnite(self):
        certificado_json = {
            "certificado_id": self.certificado_id,
            "certificado_nombre":self.certificado_nombre,
            "certificado_fecha_emision":self.certificado_fecha_emision.strftime("%Y-%m-%d"),
            "usuario_id":self.usuario_id,
            "usuario_categoria":self.usuario_categoria,
            "usuario_nombre":self.usuario_nombre,
            "usuario_estado":self.usuario_estado,
            "usuario_nota":self.usuario_nota,
            "grupo_id":self.grupo_id,
            "curso_contenido":self.curso_contenido,
            "curso_nombre":self.curso_nombre,
            "curso_fecha_inicio":self.curso_fecha_inicio.strftime("%Y-%m-%d"),
            "curso_fecha_fin":self.curso_fecha_fin.strftime("%Y-%m-%d"),
            "curso_resolucion":self.curso_resolucion,
            "curso_creditaje":self.curso_creditaje,
            "certificado_descargas":self.certificado_descargas
        }
        return certificado_json       

def add_certificado(data):
    try:       
        db.session.add(certificado(
            certificado_nombre=data["certificado_nombre"],
            certificado_fecha_emision=data["certificado_fecha"],
            usuario_id = data["usuario_id"],
            usuario_categoria = data["usuario_categoria"],
            usuario_nombre = data["usuario_nombre"],
            usuario_estado = data["usuario_estado"],
            usuario_nota = data["usuario_nota"],
            grupo_id = data["grupo_id"],
            curso_contenido = data["curso_contenido"],
            curso_nombre = data["curso_nombre"],
            curso_fecha_inicio = data["curso_fecha_inicio"],
            curso_fecha_fin = data["curso_fecha_fin"],
            curso_resolucion = data["curso_resolucion"],
            curso_creditaje = data["curso_creditaje"],
            certificado_descargas = data["certificado_descargas"]))
        db.session.commit()           
    except:        
        return False
    return True

def delete_certificado(key):
    try:
        certificado_ = certificado.query.filter_by(certificado_id=key["id"]).first()
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
    return certificado_detalle.toJsonUnite()

