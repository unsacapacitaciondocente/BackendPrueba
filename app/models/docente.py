from app.models.curso import curso
from typing import Tuple
from .bd_connection import db

class docente(db.Model):
    docente_id = db.Column(db.Integer,primary_key=True)
    doc_nombre = db.Column(db.String,nullable=True)
    doc_dni = db.Column(db.String,nullable=True)
    doc_email = db.Column(db.String,nullable=True)
    doc_celular = db.Column(db.String,nullable=True)
    doc_condicion = db.Column(db.String,nullable=True)
    doc_facultad = db.Column(db.String,nullable=True)
    doc_departamento = db.Column(db.String,nullable=True)
    doc_escuela = db.Column(db.String,nullable=True)
    doc_grado_academico = db.Column(db.String,nullable=True)
    doc_categoria = db.Column(db.String,nullable=True)
    doc_observacion = db.Column(db.String,nullable=True)
    doc_situacion = db.Column(db.String,nullable=True)

    def toJSON(self):
        docente_json ={
            "id":self.docente_id,
            "nombre":self.doc_nombre,
            "dni":self.doc_dni,
            "email":self.doc_email,
            "celular":self.doc_celular,
            "condicion":self.doc_condicion,
            "facultad":self.doc_facultad,
            "departamento":self.doc_departamento,
            "escuela":self.doc_escuela,
            "gradoacademico":self.doc_grado_academico,
            "categoria":self.doc_categoria,
            "observacion":self.doc_observacion,
            "situacion":self.doc_situacion
        }
        return docente_json

def add_docente(data):
    try:
        db.session.add(docente(doc_nombre=data["nombre"],doc_dni=data["dni"],doc_email=data["email"],doc_celular=data["celular"],doc_condicion=data["condicion"],doc_facultad=data["facultad"],doc_departamento=data["departamento"],doc_escuela=data["escuela"],doc_grado_academico=data["gradoacademico"],doc_categoria=data["categoria"],doc_observacion=data["observacion"],doc_situacion=data["situacion"]))
        db.session.commit() 
    except:
        return False
    return True

def get_all_docentes():
    arr_docentes={
        "data":[]
    }
    docentes = docente.query.all()
    for doc in docentes:
        arr_docentes["data"].append(doc.toJSON())
    return arr_docentes

def edit_docente(data):
    try:
        docente_ = docente.query.filter_by(docente_id=data["id"]).first()
        docente_.doc_nombre = data["nombre"]
        docente_.doc_dni = data["dni"]
        docente_.doc_email = data["email"]
        docente_.doc_celular = data["celular"]
        docente_.doc_condicion = data["condicion"]
        docente_.doc_facultad = data["facultad"]
        docente_.doc_departamento = data["departamento"]
        docente_.doc_escuela = data["escuela"]
        docente_.doc_grado_academico = data["gradoacademico"]
        docente_.doc_categoria = data["categoria"]
        docente_.doc_observacion = data["observacion"]
        docente_.doc_situacion = data["situacion"]
        db.session.commit()
    except:
        return False
    return True

def delete_docente(key):
    try:
        docente_ = docente.query.filter_by(docente_id=key["id"]).first()
        db.session.delete(docente_)
        db.session.commit()
    except:
        return False
    return True

def detalle_docente(id):
    docente_ = docente.query.filter_by(docente_id=id).first()
    if docente_ == None:
        return {"message":"No se ha podido obtener"}
    return docente_.toJSON()