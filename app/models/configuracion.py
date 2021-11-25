from .bd_connection import db
class configuracion(db.Model):
    configuracion_id = db.Column(db.Integer,primary_key=True)
    cof_name = db.Column(db.String,nullable=False)
    cof_value = db.Column(db.String,nullable=True)
    
    def toJSON(self):
        curso_json = {
            "id": self.configuracion_id,
            "nombre": self.cof_name,
            "valor": self.cof_value
        }
        return curso_json

def add_configuracion(data):
    try:       
        db.session.add(configuracion(cof_name=data["nombre"],cof_value=data["valor"]))
        db.session.commit()           
    except:        
        return False
    return True

def get_all_configuracion():
    arr_configuracion ={
        "data":[]
    }
    configuraciones = configuracion.query.all()
    for con in  configuraciones:
        arr_configuracion["data"].append(con.toJSON())
    return arr_configuracion

def edit_configuracion(data):
    try:
        configuracion_ = configuracion.query.filter_by(configuracion_id=data["id"]).first()
        configuracion_.cof_name  =data["nombre"]
        configuracion_.cof_value  =data["valor"]
        db.session.commit()
    except:
        return False
    return True

def delete_configuracion(key):
    try:
        configuracion_ = configuracion.query.filter_by(configuracion_id=key["id"]).first()
        db.session.delete(configuracion_)
        db.session.commit()
    except:
        return False
    return True

def detalle_configuracion(id):    
    configuracion_ = configuracion.query.filter_by(configuracion_id=id).first()    
    if configuracion_ == None:
        return {"message":"No se ha podido obtener"}
    return configuracion_.toJSON()