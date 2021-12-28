from .bd_connection import db

class ponente(db.Model):
    ponente_id = db.Column(db.Integer,primary_key=True)
    pon_nombre = db.Column(db.String,nullable=False)
    pon_correo = db.Column(db.String,nullable=True)
    pon_telefono = db.Column(db.String,nullable=True)
    pon_estado = db.Column(db.String,nullable=True)
    pon_grado_academico = db.Column(db.String, nullable=True)
    pon_especialidad = db.Column(db.String, nullable=True)
    pon_contrasena = db.Column(db.String, nullable=True)

    def toJSON(self):
        ponente_json = {
            "id":self.ponente_id,
            "nombre":self.pon_nombre,
            "correo":self.pon_correo,
            "telefono":self.pon_telefono,
            "estado":self.pon_estado,
            "grado_academico":self.pon_grado_academico,
            "especialidad":self.pon_especialidad,
            "contrasena":self.pon_contrasena
        }
        return ponente_json

def add_ponente(data):
    try:
        db.session.add(ponente(pon_nombre=data["nombre"], pon_correo=data["correo"], pon_telefono=data["telefono"], pon_estado=data["estado"], pon_grado_academico=data["grado_academico"], pon_especialidad=data["especialidad"],pon_contrasena=data["contrasena"]))
        db.session.commit()
    except:
        return False
    return True

def get_all_ponentes():
    arr_ponentes={
        "data":[]
    }
    ponentes = ponente.query.all()
    for pon in ponentes:
        arr_ponentes["data"].append(pon.toJSON())
    return arr_ponentes


def edit_ponente(data):
    try:
        ponente_ = ponente.query.filter_by(ponente_id=data["id"]).first()
        ponente_.pon_nombre=data["nombre"]
        ponente_.pon_correo=data["correo"]
        ponente_.pon_telefono=data["telefono"]
        ponente_.pon_estado=data["estado"]
        ponente_.pon_grado_academico=data["grado_academico"]
        ponente_.pon_especialidad=data["especialidad"]
        ponente_.pon_contrasena=data["contrasena"]
        db.session.commit()
    except:
        return False
    return True


def delete_ponente(key):
    try:
        ponente_ = ponente.query.filter_by(ponente_id=key["id"]).first()
        db.session.delete(ponente_)
        db.session.commit()
    except:
        return False
    return True


def detalle_ponente(id):
    ponente_ = ponente.query.filter_by(ponente_id=id).first()
    if ponente_ == None:
        return {"message":"No se ha podido obtener"}
    return ponente_.toJSON()

def buscar_PonEmail(PonEmail):
    usuario_ = ponente.query.filter_by(pon_correo=PonEmail).first()
    if usuario_ == None:
        return {"message":"No se ha podido obtener"}
    return usuario_.toJSON()

