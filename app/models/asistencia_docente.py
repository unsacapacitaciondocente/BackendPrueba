from .bd_connection import db
import datetime

class asistencia_docente(db.Model):
    asistencia_day_id = db.Column(db.Integer,primary_key=True)
    asi_doc_fecha = db.Column(db.Date,nullable=False)
    asistencia_id = db.Column(db.Integer,nullable=False)
    asi_doc_comentario = db.Column(db.String,nullable=False)
    asi_doc_estado = db.Column(db.Boolean,nullable=False)
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
       
        db.session.add(asistencia_docente(asi_doc_fecha=datetime.datetime.strptime(data["fecha"],'%Y-%m-%d'),asistencia_id=data["asistencia_id"],asi_doc_comentario=data["comentario"],asi_doc_estado=data["estado"],docente_id=data["docente_id"]))
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
