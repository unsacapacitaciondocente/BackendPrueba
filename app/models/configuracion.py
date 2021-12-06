from .bd_connection import db
class configuracion(db.Model):
    configuracion_id = db.Column(db.Integer,primary_key=True)
    name_1 = db.Column(db.String,nullable=True)
    name_2 = db.Column(db.String,nullable=True)
    name_3 = db.Column(db.String,nullable=True)
    name_4 = db.Column(db.String,nullable=True)
    name_5 = db.Column(db.String,nullable=True)
    name_6 = db.Column(db.String,nullable=True)
    value_1 = db.Column(db.String,nullable=True)
    value_2 = db.Column(db.String,nullable=True)
    value_3 = db.Column(db.String,nullable=True)
    value_4 = db.Column(db.String,nullable=True)
    value_5 = db.Column(db.String,nullable=True)
    value_6 = db.Column(db.String,nullable=True)
    estado_1 = db.Column(db.Boolean,nullable=True)
    estado_2 = db.Column(db.Boolean,nullable=True)
    estado_3 = db.Column(db.Boolean,nullable=True)
    estado_4 = db.Column(db.Boolean,nullable=True)
    estado_5 = db.Column(db.Boolean,nullable=True)
    estado_6 = db.Column(db.Boolean,nullable=True)
    certificado = db.Column(db.String,nullable=True)

    
    def toJSON(self):
        curso_json = {
            "id": self.configuracion_id,
            "nombre_1": self.name_1,
            "nombre_2": self.name_2,
            "nombre_3": self.name_3,
            "nombre_4": self.name_4,
            "nombre_5": self.name_5,
            "nombre_6": self.name_6,
            "valor_1": self.value_1,
            "valor_2": self.value_2,
            "valor_3": self.value_3,
            "valor_4": self.value_4,
            "valor_5": self.value_5,
            "valor_6": self.value_6,
            "estado_1":self.estado_1,
            "estado_2":self.estado_2,
            "estado_3":self.estado_3,
            "estado_4":self.estado_4,
            "estado_5":self.estado_5,
            "estado_6":self.estado_6,
            "certificado":self.certificado
        }
        return curso_json

def add_configuracion(data):
    try:       
        db.session.add(configuracion(
                name_1 = data["nombre_1"],
                name_2 = data["nombre_2"],
                name_3 = data["nombre_3"],
                name_4 = data["nombre_4"],
                name_5 = data["nombre_5"],
                name_6 = data["nombre_6"],
                value_1 = data["valor_1"],
                value_2 = data["valor_2"],
                value_3 = data["valor_3"],
                value_4 = data["valor_4"],
                value_5 = data["valor_5"],
                value_6 = data["valor_6"],
                estado_1 = data["estado_1"],
                estado_2 = data["estado_2"],
                estado_3 = data["estado_3"],
                estado_4 = data["estado_4"],
                estado_5 = data["estado_5"],
                estado_6 = data["estado_6"],
                certificado = data["certificado"]
        ))
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
        configuracion_.name_1  = data["nombre_1"]
        configuracion_.name_2  = data["nombre_2"]
        configuracion_.name_3  = data["nombre_3"]
        configuracion_.name_4  = data["nombre_4"]
        configuracion_.name_5  = data["nombre_5"]
        configuracion_.name_6  = data["nombre_6"]
        configuracion_.value_1  = data["valor_1"]
        configuracion_.value_2  = data["valor_2"]
        configuracion_.value_3  = data["valor_3"]
        configuracion_.value_4  = data["valor_4"]
        configuracion_.value_5  = data["valor_5"]
        configuracion_.value_6  = data["valor_6"]
        configuracion_.estado_1  = data["estado_1"]
        configuracion_.estado_2  = data["estado_2"]
        configuracion_.estado_3  = data["estado_3"]
        configuracion_.estado_4  = data["estado_4"]
        configuracion_.estado_5  = data["estado_5"]
        configuracion_.estado_6  = data["estado_6"]
        configuracion_.certificado = data["certificado"]
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