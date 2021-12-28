from .bd_connection import db
import datetime

class grupo(db.Model):
    grupo_id = db.Column(db.Integer,primary_key=True)
    ponente_id = db.Column(db.Integer,nullable=False)
    gru_nombre = db.Column(db.String,nullable=False)
    curso_capacitacion_id = db.Column(db.Integer,nullable=False)
    gru_estado = db.Column(db.String,nullable=False)
    gru_hora_inicio = db.Column(db.String,nullable=False)
    gru_hora_final = db.Column(db.String,nullable=False)
    gru_horario = db.Column(db.String,nullable=False)
    gru_observaciones = db.Column(db.String,nullable=False)


    def toJSON(self):
        grupo_json = {
            "id": self.grupo_id,
            "ponente_id": self.ponente_id,
            "nombre": self.gru_nombre,
            "curso_capacitacion_id": self.curso_capacitacion_id,
            "estado": self.gru_estado,
            "hora_inicio": self.gru_hora_inicio,
            "hora_final": self.gru_hora_final,
            "horario" : self.gru_horario,
            "observaciones" : self.gru_observaciones
        }
        return grupo_json
  
def add_grupo(data):
    try:
        db.session.add(grupo(ponente_id=data["ponente_id"],gru_nombre=data["nombre"],curso_capacitacion_id=data["curso_capacitacion_id"],gru_estado=data["estado"],gru_hora_inicio=data["fecha_inicio"],gru_hora_final=data["hora_final"],gru_horario=data["horario"],gru_observaciones=data["observaciones"]))
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
        grupo_.gru_hora_inicio=data["hora_inicio"]
        grupo_.gru_hora_final=data["hora_final"]
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
