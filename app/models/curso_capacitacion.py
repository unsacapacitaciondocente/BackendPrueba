from .bd_connection import db
import datetime

class curso_capacitacion(db.Model):
    curso_capacitacion_id = db.Column(db.Integer,primary_key=True)
    cur_cap_nombre = db.Column(db.String,nullable=False)
    cur_cap_descripcion = db.Column(db.String,nullable=False)
    cur_cap_estado = db.Column(db.String,nullable=False)
    resolucion_id = db.Column(db.Integer,nullable=False)
    cur_cap_fecha = db.Column(db.Date,nullable=False)
    cur_cap_creditaje= db.Column(db.Float,nullable=False)
    cur_cap_horas= db.Column(db.Float,nullable=False)
    cur_cap_presupuesto= db.Column(db.Float,nullable=False)
    cur_cap_situacion = db.Column(db.String,nullable=False)
    cur_cap_observacion = db.Column(db.String,nullable=False)

    def toJSON(self):
        curso_capacitacion_json = {
            "id": self.curso_capacitacion_id,
            "nombre": self.cur_cap_nombre,
            "descripcion": self.cur_cap_descripcion,
            "estado": self.cur_cap_estado,
            "resolucion_id":self.resolucion_id,
            "fecha": self.cur_cap_fecha.strftime("%Y-%m-%d"),
            "creditaje": self.cur_cap_creditaje,
            "horas": self.cur_cap_horas,
            "presupuesto": self.cur_cap_presupuesto,
            "situacion": self.cur_cap_situacion,
            "observacion": self.cur_cap_observacion
            
        }
        return curso_capacitacion_json
  
def add_curso_capacitacion(data):
    try:
        db.session.add(curso_capacitacion(cur_cap_nombre=data["nombre"],cur_cap_descripcion=data["descripcion"],cur_cap_estado=data["estado"],resolucion_id=data["resolucion_id"],cur_cap_fecha=datetime.datetime.strptime(data["fecha"],'%Y-%m-%d'),cur_cap_creditaje=data["creditaje"],cur_cap_horas=data["horas"],cur_cap_presupuesto=data["presupuesto"],cur_cap_situacion=data["situacion"],cur_cap_observacion=data["observacion"]))
        db.session.commit()   
    except:
        
        return False
    return True

def get_all_curso_capacitacion():
    arr_cursos_capacitacion ={
        "data":[]
    }
    cursos_capaticacion=curso_capacitacion.query.all()
    for cur in  cursos_capaticacion:
        arr_cursos_capacitacion["data"].append(cur.toJSON())
    return arr_cursos_capacitacion

def edit_curso_capacitacion(data):
    try:
        curso_capacitacion_ = curso_capacitacion.query.filter_by(curso_capacitacion_id=data["id"]).first()
        curso_capacitacion_.cur_cap_nombre=data["nombre"]
        curso_capacitacion_.cur_cap_descripcion=data["descripcion"]
        curso_capacitacion_.cur_cap_estado=data["estado"]
        curso_capacitacion_.resolucion_id=data["resolucion"]
        curso_capacitacion_.cur_cap_fecha=data["fecha"]
        curso_capacitacion_.cur_cap_creditaje=data["creditaje"]
        curso_capacitacion_.cur_cap_horas=data["horas"]
        curso_capacitacion_.cur_cap_presupuesto=data["presupuesto"]
        curso_capacitacion_.cur_cap_situacion=data["situacion"]
        curso_capacitacion_.cur_cap_observacion=data["observacion"]
        db.session.commit()
    except:
        return False
    return True

def delete_curso_capacitacion(key):
    try:
        curso_capacitacion_ = curso_capacitacion.query.filter_by(curso_id=key["id"]).first()
        db.session.delete(curso_capacitacion_)
        db.session.commit()
    except:
        return False
    return True

def detalle_curso_capacitacion(id):
    
    curso_capacitacion_ = curso_capacitacion.query.filter_by(curso_id=id).first()
    
    if curso_capacitacion_ == None:
        return {"message":"No se ha podido obtener"}
    return curso_capacitacion_.toJSON()
