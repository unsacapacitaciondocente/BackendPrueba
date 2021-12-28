from operator import truediv
from .bd_connection import db
from .lista_participante import lista_participante
from .docente import docente
from .curso_capacitacion import curso_capacitacion
from .grupo import grupo

class curso_seguimiento():
    pass
    
def get_curso_seguimiento(id):
    
    query_cur_seg_detalle= """
    select g.grupo_id, g.gru_nombre, g.gru_estado, g.gru_horario, g.gru_observaciones, g.gru_hora_inicio, g.gru_hora_final, c.curso_capacitacion_id, c.cur_cap_resolucion, c.cur_cap_nombre, p.ponente_id, p.pon_nombre 
    from grupo g, curso_capacitacion c, ponente p 
    where g.ponente_id = p.ponente_id and c.curso_capacitacion_id = g.curso_capacitacion_id  
    and grupo_id = :grupo_id
    """
    
    try:
    
        bind_data = {'grupo_id': id}
        result_dict = {"data":[]}

        result = db.session.execute(query_cur_seg_detalle, bind_data)
        for row in result:
            result_dict['data'].append({
                'gru_id': row[0],
                'gru_nom': row[1],
                'gru_est': row[2],
                'gru_hor': row[3],
                'gru_obs': row[4],
                'gru_hor_ini': row[5],
                'gru_hor_fin': row[6],
                'cur_cap_id': row[7],
                'cur_cap_res': row[8],
                'cur_cap_nom': row[9],
                'pon_id': row[10],
                'pon_nombre': row[11]
            })
        return result_dict

    except:   
        return {"message":"No se ha podido obtener"}

def get_cursos_seguimiento():

    # esta parte imaginamos un poco que CUR_CAP_ESTADO = 1, SON LOS CURSOS EN DESARROLLO
    query_cur_seg= """ select c.curso_capacitacion_id, c.cur_cap_nombre, g.grupo_id, g.gru_nombre, p.ponente_id, p.pon_nombre,g.gru_horario, c.cur_cap_resolucion, g.gru_observaciones, g.gru_estado, g.gru_hora_inicio, g.gru_hora_final 
    from grupo g, curso_capacitacion c, ponente p
    where g.ponente_id = p.ponente_id and c.curso_capacitacion_id = g.curso_capacitacion_id and c.cur_cap_estado = :curso_desarrollo and p.pon_estado = :estado_ponente; 
    """
    
    try:
        # esta parte imaginamos un poco que CUR_CAP_ESTADO = 1, SON LOS CURSOS EN DESARROLLO
        bind_data = {'curso_desarrollo':"En proceso",'estado_ponente':"En curso"}
        result_dict = {"data":[]}

        result = db.session.execute(query_cur_seg, bind_data)
        for row in result:
            result_dict['data'].append({
                'cur_cap_id': row[0],
                'cur_cap_nom': row[1],
                'gru_id': row[2],
                'gru_nom': row[3],
                'pon_id': row[4],
                'pon_nom': row[5],
                'gru_hor': row[6],
                'cur_cap_res': row[7],
                'gru_obs': row[8],
                'gru_est': row[9],
                'gru_hor_ini': row[10],
                'gru_hor_fin': row[11]
            })
        return result_dict

    except:   
        return False 

def add_curso_seguimiento(data):

    query_add_cur_seg = """ INSERT INTO grupo(
	ponente_id, gru_nombre, curso_capacitacion_id, gru_estado, gru_horario, gru_observaciones, gru_hora_inicio, gru_hora_final) 
	VALUES (:pon_id, :gru_nom, :cur_cap_id, :gru_est, :gru_hor, :gru_obs, :gru_hor_ini, :gru_hor_fin); 
    """

    try:

        bind_data = {
            'pon_id': data["pon_id"],
            'gru_nom': data["gru_nom"],
            'cur_cap_id': data["cur_cap_id"],
            'gru_est': data["gru_est"],
            'gru_hor': data["gru_hor"],
            'gru_obs': data["gru_obs"],
            'gru_hor_ini': data["gru_hor_ini"],
            'gru_hor_fin': data["gru_hor_fin"]
            
        }
        
        db.session.execute(query_add_cur_seg, bind_data)
        db.session.commit()
        return True  
    except:
        return False
def edit_curso_seguimiento(data):

    query_add_cur_seg = """ UPDATE public.grupo
	SET ponente_id= :pon_id, gru_nombre= :gru_nom, curso_capacitacion_id= :cur_cap_id, gru_estado= :gru_est, gru_horario= :gru_hor, gru_observaciones= :gru_obs, gru_hora_inicio= :gru_hor_ini, gru_hora_final= :gru_hor_fin 
	WHERE grupo_id = :gru_id; 
    """

    try:

        bind_data = {
            'gru_id': data['gru_id'],
            'pon_id': data["pon_id"],
            'gru_nom': data["gru_nom"],
            'cur_cap_id': data["cur_cap_id"],
            'gru_est': data["gru_est"],
            'gru_hor': data["gru_hor"],
            'gru_obs': data["gru_obs"],
            'gru_hor_ini': data["gru_hor_ini"],
            'gru_hor_fin': data["gru_hor_fin"]
            
        }
        
        db.session.execute(query_add_cur_seg, bind_data)
        db.session.commit()
        return True  
    except:
        return False

def get_docentes_por_curso(id):
    
    query_cur_seg_doc = """ 
    SELECT c.cur_cap_nombre, c.curso_capacitacion_id, d.doc_dni, d.doc_email, d.docente_id, d.doc_nombre, d.doc_departamento, d.doc_escuela, d.doc_facultad, g.grupo_id, g.gru_nombre , l.lista_participante_id 
    FROM lista_participante l, docente d, grupo g, curso_capacitacion c 
    WHERE l.docente_id = d.docente_id and g.grupo_id = l.grupo_id and g.curso_capacitacion_id = c.curso_capacitacion_id 
	and l.grupo_id = :gru_id and lis_par_estado = 'Activo' 
    """
    
    try:
        
        bind_data = {'gru_id':id}
        result_dict = {"data":[]}

        result = db.session.execute(query_cur_seg_doc, bind_data)
        for row in result:
            result_dict['data'].append({
                'cur_cap_nombre': row[0],
                'curso_capacitacion_id': row[1],
                'docente_dni': row[2],
                'docente_email': row[3],
                'docente_id': row[4],
                'docente_nombre': row[5],
                'docente_par_departamento': row[6],
                'docente_par_escuela': row[7],
                'docente_par_facultad': row[8],
                'grupo_id':row[9],
                'grupo_nom':row[10],
                'lista_participante_id':row[11]
            })
        return result_dict
    except:   
        return False 
    
def delete_grupo(key):

    query_del_cur_seg = """ DELETE FROM grupo 
    WHERE grupo.grupo_id = :gru_id;
    """

    try:
        bind_data = {'gru_id':key["id"]}
        result_dict = {"data":[]}

        db.session.execute(query_del_cur_seg, bind_data)
        db.session.commit()
    except:
        return False
    return True

def getCursosPorEstado(data):
    
    query_cur_cap_est= """ select curso_capacitacion_id, cur_cap_nombre, cur_cap_resolucion from curso_capacitacion 
    where cur_cap_estado = :cur_cap_estado
    """
    
    try:
        
        bind_data = {'cur_cap_estado': data["cur_cap_estado"]}
        result_dict = {"data":[]}

        result = db.session.execute(query_cur_cap_est, bind_data)
        for row in result:
            result_dict['data'].append({
                'cur_cap_id': row[0],
                'cur_cap_nom': row[1],
                'cur_cap_resolucion': row[2]
            })
        return result_dict

    except:   
        return False 

def getPonentesActivos():
    # esta parte imaginamos un poco que CUR_CAP_ESTADO = 1, SON LOS CURSOS EN DESARROLLO
    query_cur_cap_est= """ select ponente_id, pon_nombre from ponente 
    where pon_estado = 'activo'
    """
    
    try:
        result_dict = {"data":[]}

        result = db.session.execute(query_cur_cap_est)
        for row in result:
            result_dict['data'].append({
                'pon_id': row[0],
                'pon_nom': row[1]
            })
        return result_dict

    except:   
        return False

def matricularDocente(data):

    query_get_data_docente = """ 
    select doc_escuela, doc_departamento, doc_facultad from docente where docente_id = :docente_id
    """
    escuela = ""
    departamento = ""
    facultad = ""

    query_matricular_docente= """
    INSERT INTO lista_participante(
	grupo_id, docente_id, lis_par_escuela, lis_par_departamento, lis_par_facultad, lis_par_estado, lis_par_condicion, lis_nota, lis_par_asistencia_actual, lis_par_asistencia_total, lis_par_horas_acumuladas)
	VALUES (:grupo_id, :docente_id, :lis_par_escuela, :lis_par_departamento, :lis_par_facultad, 'Activo', 'Desaprobado', 0, 0, 0, 0);
    """

    try:

        bind_data = {'docente_id': data["docente_id"]}

        result = db.session.execute(query_get_data_docente, bind_data)

        for row in result: 
            escuela = row[0]
            departamento = row[1]
            facultad = row[2]

        bind_data = {
            'grupo_id': data["grupo_id"],
            'docente_id': data["docente_id"],
            'lis_par_escuela': escuela,
            'lis_par_departamento': departamento,
            'lis_par_facultad': facultad,
        }

        result = db.session.execute(query_matricular_docente, bind_data)
        db.session.commit()
        return True
    except:
        return False

def preMatricularDocente(data):

    query_get_data_docente = """ 
    select doc_escuela, doc_departamento, doc_facultad from docente where docente_id = :docente_id
    """
    escuela = ""
    departamento = ""
    facultad = ""

    query_matricular_docente= """
    INSERT INTO lista_participante(
	grupo_id, docente_id, lis_par_escuela, lis_par_departamento, lis_par_facultad, lis_par_estado, lis_par_condicion, lis_nota, lis_par_asistencia_actual, lis_par_asistencia_total, lis_par_horas_acumuladas)
	VALUES (:grupo_id, :docente_id, :lis_par_escuela, :lis_par_departamento, :lis_par_facultad, 'Inactivo', 'Desaprobado', 0, 0, 0, 0);
    """

    try:

        bind_data = {'docente_id': data["docente_id"]}

        result = db.session.execute(query_get_data_docente, bind_data)

        for row in result: 
            escuela = row[0]
            departamento = row[1]
            facultad = row[2]

        bind_data = {
            'grupo_id': data["grupo_id"],
            'docente_id': data["docente_id"],
            'lis_par_escuela': escuela,
            'lis_par_departamento': departamento,
            'lis_par_facultad': facultad,
        }

        result = db.session.execute(query_matricular_docente, bind_data)
        db.session.commit()
        return True
    except:
        return False


def desmatricularDocente(data):

    query_desmatricular_docente = """ 
    delete from lista_participante where lista_participante_id = :lis_par_id
    """

    try:
        bind_data = {'lis_par_id':data["lista_participante_id"]}

        db.session.execute(query_desmatricular_docente, bind_data)
        db.session.commit()
    except:
        return False
    return True

def cambiarEstado(data):
    query_cambiar_estado = """ 
    UPDATE public.lista_participante 
    SET lis_par_estado = 'Activo' 
    WHERE lista_participante_id = :lis_par_id 
    """

    try:
        bind_data = {'lis_par_id':data["lista_participante_id"]}

        db.session.execute(query_cambiar_estado, bind_data)
        db.session.commit()
    except:
        return False
    return True


def getListaPreMatriculados():
    pre_matriculados={
        "registros" : []
    }
    pre_inscritos = lista_participante.query.filter_by(lis_par_estado="Inactivo").all()
    
    for inscrito in pre_inscritos:
        pre_matriculado={
            'lista_participante_id':'',
            'grupo_id':'',
            'grupo_nom':'',
            'docente_id':'',
            'docente_email':'',
            'docente_nombre'
            'docente_dni':'',
            'docente_par_escuela':'',
            'docente_par_departamento':'',
            'docente_par_facultad':'',
            'curso_capacitacion_id':'',
            'cur_cap_nombre':''
        }
        pre_matriculado['lista_participante_id']=inscrito.lista_participante_id
        pre_matriculado['grupo_id']=inscrito.grupo_id
        grupo_aux=grupo.query.filter_by(grupo_id=inscrito.grupo_id).first()
        pre_matriculado['grupo_nom']=grupo_aux.gru_nombre
        pre_matriculado['docente_id']=inscrito.docente_id
        docente_aux=docente.query.filter_by(docente_id=inscrito.docente_id).first()
        pre_matriculado['docente_email']=docente_aux.doc_email
        pre_matriculado['docente_nombre']=docente_aux.doc_nombre
        pre_matriculado['docente_dni']=docente_aux.doc_dni
        pre_matriculado['docente_par_escuela']=docente_aux.doc_escuela
        pre_matriculado['docente_par_departamento']=docente_aux.doc_departamento
        pre_matriculado['docente_par_facultad']=docente_aux.doc_facultad
        pre_matriculado['curso_capacitacion_id']=grupo_aux.curso_capacitacion_id
        curso_aux=curso_capacitacion.query.filter_by(curso_capacitacion_id=grupo_aux.curso_capacitacion_id).first()
        pre_matriculado['cur_cap_nombre']=curso_aux.cur_cap_nombre
        pre_matriculados['registros'].append(pre_matriculado)
        
    return pre_matriculados['registros']

def getPreMatriculado(id):
 
    inscrito = lista_participante.query.filter_by(lista_participante_id=id).first()
    
    if inscrito == None:
        return {"message":"No se ha podido obtener"}
    
    pre_matriculado={
        'grupo_id':'',
        'grupo_nom':'',
        'docente_id':'',
        'docente_email':'',
        'docente_nombre'
        'docente_dni':'',
        'docente_par_escuela':'',
        'docente_par_departamento':'',
        'docente_par_facultad':'',
        'curso_capacitacion_id':'',
        'cur_cap_nombre':''
    }
        
    pre_matriculado['grupo_id']=inscrito.grupo_id
    grupo_aux=grupo.query.filter_by(grupo_id=inscrito.grupo_id).first()
    pre_matriculado['grupo_nom']=grupo_aux.gru_nombre
    pre_matriculado['docente_id']=inscrito.docente_id
    docente_aux=docente.query.filter_by(docente_id=inscrito.docente_id).first()
    pre_matriculado['docente_email']=docente_aux.doc_email
    pre_matriculado['docente_nombre']=docente_aux.doc_nombre
    pre_matriculado['docente_dni']=docente_aux.doc_dni
    pre_matriculado['docente_par_escuela']=docente_aux.doc_escuela
    pre_matriculado['docente_par_departamento']=docente_aux.doc_departamento
    pre_matriculado['docente_par_facultad']=docente_aux.doc_facultad
    pre_matriculado['curso_capacitacion_id']=grupo_aux.curso_capacitacion_id
    curso_aux=curso_capacitacion.query.filter_by(curso_capacitacion_id=grupo_aux.curso_capacitacion_id).first()
    pre_matriculado['cur_cap_nombre']=curso_aux.cur_cap_nombre
        
    return pre_matriculado