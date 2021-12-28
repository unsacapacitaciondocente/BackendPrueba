from .bd_connection import db
import datetime

class lista_participante(db.Model):
    grupo_id = db.Column(db.Integer,nullable=False)
    docente_id = db.Column(db.Integer,nullable=False)
    lis_par_escuela = db.Column(db.String,nullable=False)
    lis_par_departamento = db.Column(db.String,nullable=False)
    lis_par_facultad = db.Column(db.String,nullable=False)
    lis_par_estado = db.Column(db.String,nullable=False)
    lis_par_condicion = db.Column(db.String,nullable=False)
    lis_nota = db.Column(db.Float,nullable=False)
    lis_par_asistencia_actual = db.Column(db.Integer,nullable=False)
    lis_par_asistencia_total = db.Column(db.Integer,nullable=False)
    lis_par_horas_acumuladas = db.Column(db.Float,nullable=False)
    lista_participante_id = db.Column(db.Integer,primary_key=True)



    def toJSON(self):
        grupo_json = {
            "id": self.lista_participante_id,
            "grupo_id": self.grupo_id ,
            "docente_id": self.docente_id ,
            "escuela": self.lis_par_escuela ,
            "departamento": self.lis_par_departamento ,
            "facultad": self.lis_par_facultad ,
            "estado": self.lis_par_estado ,
            "condicion" : self.lis_par_condicion ,
            "nota" : self.lis_nota ,
            "asistencia_actual" : self.lis_par_asistencia_actual,
            "asistencia_total" : self.lis_par_asistencia_total,
            "horas_acumuladas" : self.lis_par_horas_acumuladas
        }
        return grupo_json

def add_lista_participante(data):
    try:
        db.session.add(lista_participante(grupo_id=data["grupo_id"],docente_id=data["docente_id"],lis_par_escuela=data["escuela"],lis_par_departamento=data["departamento"],lis_par_facultad=data["facultad"],lis_par_estado=data["estado"],lis_par_condicion=data["condicion"],lis_nota=data["nota"],lis_par_asistencia_actual=data['asistencia_actual'],lis_par_asistencia_total=data['asistencia_total'],lis_par_horas_acumuladas=data['horas_acumuladas']))
        db.session.commit()   
    except:
        print("llego hasta agregar lista particpante")
        return False
    return True

def edit_lista_participante(data):
    try:
        participante = lista_participante.query.filter_by(lista_participante_id=data["id"]).first()
        participante.grupo_id=data["grupo_id"]
        participante.docente_id=data["docente_id"]
        participante.lis_par_escuela=data["escuela"]
        participante.lis_par_departamento=data["departamento"]
        participante.lis_par_facultad=data["facultad"]
        participante.lis_par_estado=data["estado"]
        participante.lis_par_condicion=data["condicion"]
        participante.lis_nota = data["nota"]
        participante.lis_par_asistencia_actual=data["asistencia_actual"]
        participante.lis_par_asistencia_total=data["asistencia_total"]
        participante.lis_par_horas_acumuladas=data["horas_acumuladas"]
        db.session.commit()
    except:
        return False
    return True