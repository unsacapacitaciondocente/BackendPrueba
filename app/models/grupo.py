from .bd_connection import db
import datetime

class grupo(db.Model):
    grupo_id = db.Column(db.Integer,primary_key=True)
    ponente_id = db.Column(db.Integer,nullable=False)
    gru_nombre = db.Column(db.String,nullable=False)
    curso_capacitacion_id = db.Column(db.Integer,nullable=False)
    gru_estado = db.Column(db.String,nullable=False)
    gru_fecha_inicio = db.Column(db.Date,nullable=False)
    gru_fecha_final = db.Column(db.Date,nullable=False)
    gru_horario = db.Column(db.String,nullable=False)
    gru_observaciones = db.Column(db.String,nullable=False)


    def toJSON(self):
        grupo_json = {
            "id": self.grupo_id,
            "ponente_id": self.ponente_id,
            "nombre": self.gru_nombre,
            "curso_capacitacion_id": self.curso_capacitacion_id,
            "estado": self.gru_estado,
            "fecha_inicio": self.gru_fecha_inicio.strftime("%Y-%m-%d"),
            "fecha_final": self.gru_fecha_final.strftime("%Y-%m-%d"),
            "horario" : self.gru_horario,
            "observaciones" : self.gru_observaciones
        }
        return grupo_json
  
def add_grupo(data):
    try:
        db.session.add(grupo(ponente_id=data["ponente_id"],gru_nombre=data["nombre"],curso_capacitacion_id=data["curso_capacitacion_id"],gru_estado=data["estado"],gru_fecha_inicio=datetime.datetime.strptime(data["fecha_inicio"],'%Y-%m-%d'),gru_fecha_final=datetime.datetime.strptime(data["fecha_final"],'%Y-%m-%d'),gru_horario=data["horario"],gru_observaciones=data["observaciones"]))
        db.session.commit()   
    except:
        
        return False
    return True

def get_all_grupo():
    arr_grupo ={
        "data":[]
    }
    grupos=grupo.query.all()
    for cur in  grupos:
        arr_grupo["data"].append(cur.toJSON())
    return arr_grupo

def edit_grupo(data):
    try:
        grupo_ = grupo.query.filter_by(grupo_id=data["id"]).first()
        grupo_.ponente_id=data["ponente_id"]
        grupo_.gru_nombre=data["nombre"]
        grupo_.curso_capacitacion_id=data["curso_capacitacion_id"]
        grupo_.gru_estado=data["estado"]
        grupo_.gru_fecha_inicio=data["fecha_inicio"]
        grupo_.gru_fecha_final=data["fecha_final"]
        grupo_.gru_horario=data["horario"]
        grupo_.gru_observaciones=data["observaciones"]
        db.session.commit()
    except:
        return False
    return True

def delete_grupo(key):
    try:
        grupo_ = grupo.query.filter_by(grupo_id=key["id"]).first()
        db.session.delete(grupo_)
        db.session.commit()
    except:
        return False
    return True

def detalle_grupo(id):
    
    grupo_ = grupo.query.filter_by(grupo_id=id).first()
    
    if grupo_ == None:
        return {"message":"No se ha podido obtener"}
    return grupo_.toJSON()
