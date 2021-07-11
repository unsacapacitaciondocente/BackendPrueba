from .bd_connection import db

class curso(db.Model):
    curso_id = db.Column(db.Integer,primary_key=True)
    cur_nombre = db.Column(db.String,nullable=False)
    cur_descripcion = db.Column(db.String,nullable=True)
    cur_estado = db.Column(db.Integer,nullable=False)
    cur_resolucion = db.Column(db.Integer,nullable=True)

    def toJSON(self):
        curso_json = {
            "id": self.curso_id,
            "nombre": self.cur_nombre,
            "descripcion": self.cur_descripcion,
            "estado": self.cur_estado,
            "resolucion":self.cur_resolucion
        }
        return curso_json
  
def add_curso(data):
    try:
        db.session.add(curso(cur_nombre=data["nombre"],cur_descripcion=data["descripcion"],cur_estado=data["estado"],cur_resolucion=data["resolucion"]))
        db.session.commit()           
    except:
        return False
    return True

def get_all_cursos():
    arr_cursos ={
        "data":[]
    }
    cursos = curso.query.all()
    for cur in  cursos:
        arr_cursos["data"].append(cur.toJSON())
    return arr_cursos

def edit_curso(data):
    try:
        curso_ = curso.query.filter_by(curso_id=data["curso_id"]).first()
        curso_.cur_nombre=data["nombre"]
        curso_.cur_descripcion=data["descripcion"]
        curso_.cur_estado=data["estado"]
        curso_.cur_resolucion=data["resolucion"]
        db.session.commit()
    except:
        return False
    return True

def delete_curso(key):
    try:
        curso_ = curso.query.filter_by(curso_id=key["id"]).first()
        db.session.delete(curso_)
        db.session.commit()
    except:
        return False
    return True

def detalle_curso(key):
    
    curso_ = curso.query.filter_by(curso_id=key["id"]).first()
    
    if curso_ == None:
        return {"message":"No se ha podido obtener"}
    return curso_.toJSON()

# db.session.add(curso(cur_nombre="dying is good",cur_descripcion="este es un curso",cur_estado=1,cur_resolucion="D48 UNSA"))
# db.session.commit()