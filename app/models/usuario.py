from .bd_connection import db
from typing import Tuple

class usuario(db.Model):
    usuario_id = db.Column(db.Integer,primary_key=True)
    us_username = db.Column(db.String,nullable=True)
    us_password = db.Column(db.String,nullable=True)
    us_nombre = db.Column(db.String,nullable=True) 
    us_correo= db.Column(db.String,nullable=True)
    us_dni = db.Column(db.String,nullable=True)

    def toJSON(self):
        usuario_json = {
            "id": self.usuario_id,
            "username": self.us_username,
            "password": self.us_password,
            "nombre": self.us_nombre,
            "correo": self.us_correo,
            "dni": self.us_dni
        }
        return usuario_json

def add_usuario(data):
    try:
        db.session.add(usuario(us_username=data['username'],us_password=data['password'],us_nombre=data['nombre'],us_correo=data['correo'],us_dni=data['dni']))
        db.session.commit()
    except:
        return False
    return True

def get_all_usuarios():
    arr_usuarios={
        "data":[]
    }
    usuarios = usuario.query.all()
    for user in usuarios:
        arr_usuarios["data"].append(user.toJSON())
    return arr_usuarios

def edit_usuario(data):
    try:
        usuario_ = usuario.query.filter_by(usuario_id=data["id"]).first()
        usuario_.us_username=data["username"]
        usuario_.us_password=data["password"]
        usuario_.us_nombre=data['nombre']
        usuario_.us_correo=data['correo']
        usuario_.us_dni=data['dni']
        db.session.commit()
    except:
        return False
    return True


def delete_usuario(key):
    try:
        usuario_ = usuario.query.filter_by(usuario_id=key["id"]).first()
        db.session.delete(usuario_)
        db.session.commit()
    except:
        return False
    return True


def detalle_usuario(id):
    usuario_ = usuario.query.filter_by(usuario_id=id).first()
    if usuario_ == None:
        return {"message":"No se ha podido obtener"}
    return usuario_.toJSON()

def buscar_username(username):
    usuario_ = usuario.query.filter_by(us_username=username).first()
    if usuario_ == None:
        return {"message":"No se ha podido obtener"}
    return usuario_.toJSON()

def authentication(username,password):
    print('__authenticate')
    usuario_ = usuario.query.filter_by(us_username=username).first()
    if usuario_.id==password:
        return usuario_

def identity(payload):
    print('identity')
    user_id=payload['identity   ']
    print(user_id)
    usuario_ = usuario.query.filter_by(usuario_id=user_id).first()
    return usuario_

