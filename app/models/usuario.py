from .bd_connection import db

class usuario(db.Model):
    usuario_id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String,nullable=False)
    password = db.Column(db.String,nullable=True)

    def toJSON(self):
        usuario_json = {
            "id": self.usuario_id,
            "username": self.username,
            "password": self.password,
           
        }
        return usuario_json

def add_usuario(data):
    try:
        db.session.add(usuario(username=data["username"], password=data["password"]))
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
        usuario_ = usuario.query.filter_by(usuario_id=data["usuario_id"]).first()
        usuario_.username=data["username"]
        password_.password=data["password"]
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
    usuario_ = usuario.query.filter_by(username=username).first()
    if usuario_ == None:
        return {"message":"No se ha podido obtener"}
    return usuario_.toJSON()

def authentication(username,password):
    print('__authenticate')
    usuario_ = usuario.query.filter_by(username=username).first()
    if usuario_.id==password:
        return usuario_

def identity(payload):
    print('identity')
    user_id=payload['identity   ']
    print(user_id)
    usuario_ = usuario.query.filter_by(usuario_id=user_id).first()
    return usuario_

