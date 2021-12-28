"""
from .bd_connection import db

class documento_ponente(db.Model):
    documento_ponente_id = db.Column(db.Integer,primary_key=True)
    doc_pon_nombre = db.Column(db.String,nullable=False)
    ponente_id = db.Column(db.Integer,nullable=False)
    doc_log_url = db.Column(db.String,nullable=False)
  

    def toJSON(self):
        documento_ponente_json = {
            "id": self.documento_ponente_id,
            "nombre": self.doc_pon_nombre,
            "ponente_id": self.ponente_id,
            "log_url": self.doc_log_url,
        }
        return documento_ponente_json
  
def add_documento_ponente(data):
    try:
       
        db.session.add(documento_ponente(doc_pon_nombre=data["nombre"],ponente_id=data["ponente_id"],doc_log_url=data["log_url"]))
        db.session.commit()           
    except:
        return False
    return True

def get_all_documento_ponente():
    arr_documento_ponente ={
        "data":[]
    }
    documento_ponentes = documento_ponente.query.all()
    for cur in  documento_ponentes:
        arr_documento_ponente["data"].append(cur.toJSON())
    return arr_documento_ponente

def edit_documento_ponente(data):
    try:
        documento_ponente_ = documento_ponente.query.filter_by(documento_ponente_id=data["id"]).first()
        documento_ponente_.doc_pon_nombre=data["nombre"]
        documento_ponente_.ponente_id=data["ponente_id"]
        documento_ponente_.doc_log_url=data["log_url"]
        db.session.commit()
    except:
        return False
    return True

def delete_documento_ponente(key):
    try:
        documento_ponente_ = documento_ponente.query.filter_by(documento_ponente_id=key["id"]).first()
        db.session.delete(documento_ponente_)
        db.session.commit()
    except:
        return False
    return True

def detalle_documento_ponente(id):
    
    documento_ponente_ = documento_ponente.query.filter_by(documento_ponente_id=id).first()
    
    if documento_ponente_ == None:
        return {"message":"No se ha podido obtener"}
    return documento_ponente_.toJSON()

    """