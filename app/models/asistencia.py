from .bd_connection import db
import datetime

class asistencia(db.Model):
    asistencia_id = db.Column(db.Integer,primary_key=True)
    asi_fecha = db.Column(db.Date,nullable=False)
    grupo_id = db.Column(db.Integer,nullable=False)
    asi_comentario = db.Column(db.String,nullable=False)
    asi_estado = db.Column(db.String,nullable=False)

    def toJSON(self):
        asistencia_json = {
            "id": self.asistencia_id,
            "fecha": self.asi_fecha.strftime("%Y-%m-%d"),
            "grupo_id": self.grupo_id,
            "comentario": self.asi_comentario,
            "estado": self.asi_estado
        }
        return asistencia_json

 
def add_asistencia(data):
    try:
       
        db.session.add(asistencia(asi_fecha=datetime.datetime.strptime(data["fecha"],'%Y-%m-%d'),grupo_id=data["grupo_id"],asi_comentario=data["comentario"],asi_estado=data["estado"]))
        db.session.commit()           
    except:
        return False
    return True

def get_all_asistencia():
    arr_asistencia ={
        "data":[]
    }
    asistencias = asistencia.query.all()
    for cur in  asistencias:
        arr_asistencia["data"].append(cur.toJSON())
    return arr_asistencia

def edit_asistencia(data):
    try:
        asistencia_ = asistencia.query.filter_by(asistencia_id=data["id"]).first()
        asistencia_.asi_fecha=data["fecha"]
        asistencia_.grupo_id=data["grupo_id"]
        asistencia_.asi_comentario=data["comentario"]
        asistencia_.asi_estado=data["estado"]
        db.session.commit()
    except:
        return False
    return True

def delete_asistencia(key):
    try:
        asistencia_ = asistencia.query.filter_by(asistencia_id=key["id"]).first()
        db.session.delete(asistencia_)
        db.session.commit()
    except:
        return False
    return True

def detalle_asistencia(id):
    
    asistencia_ = asistencia.query.filter_by(asistencia_id=id).first()

    if asistencia_ == None:
        return {"message":"No se ha podido obtener"}
    return asistencia_.toJSON()