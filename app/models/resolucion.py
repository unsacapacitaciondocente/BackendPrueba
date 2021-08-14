from .bd_connection import db

class resolucion(db.Model):
    resolucion_id = db.Column(db.Integer,primary_key=True)
    res_nombre = db.Column(db.String,nullable=True)
    res_estado = db.Column(db.String,nullable=True)
    res_fecha = db.Column(db.String,nullable=True)
    res_url = db.Column(db.String,nullable=True)
    res_numero = db.Column(db.String, nullable=True)
    res_situacion = db.Column(db.String, nullable=True)

    def toJSON(self):
        resolucion_json = {
            "id":self.resolucion_id,
            "nombre":self.res_nombre,
            "estado":self.res_estado,
            "fecha":self.res_fecha,
            "url":self.res_url,
            "numero":self.res_numero,
            "situacion":self.res_situacion
        }
        return resolucion_json

def add_resolucion(data):
    try:
        db.session.add(resolucion(res_nombre=data["nombre"], res_estado=data["estado"], res_fecha=data["fecha"], res_url=data["url"], res_numero=data["numero"], res_situacion=data["situacion"] ))
        db.session.commit()
    except:
        return False
    return True

def get_all_resoluciones():
    arr_resoluciones={
        "data":[]
    }
    resoluciones = resolucion.query.all()
    for res in resoluciones:
        arr_resoluciones["data"].append(res.toJSON())
    return arr_resoluciones


def edit_resolucion(data):
    try:
        resolucion_ = resolucion.query.filter_by(resolucion_id=data["id"]).first()
        resolucion_.res_nombre=data["nombre"]
        resolucion_.res_estado=data["estado"]
        resolucion_.res_fecha=data["fecha"]
        resolucion_.res_url=data["url"]
        resolucion_.res_numero=data["numero"]
        resolucion_.res_situacion=data["situacion"]
        db.session.commit()
    except:
        return False
    return True


def delete_resolucion(key):
    try:
        resolucion_ = resolucion.query.filter_by(resolucion_id=key["id"]).first()
        db.session.delete(resolucion_)
        db.session.commit()
    except:
        return False
    return True


def detalle_resolucion(id):
    resolucion_ = resolucion.query.filter_by(resolucion_id=id).first()
    if resolucion_ == None:
        return {"message":"No se ha podido obtener"}
    return resolucion_.toJSON()