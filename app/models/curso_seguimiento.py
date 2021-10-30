from .bd_connection import db

class curso_seguimiento():
    pass
    
    
def get_cursos_seguimiento():

    # esta parte imaginamos un poco que CUR_CAP_ESTADO = 1, SON LOS CURSOS EN DESARROLLO
    query_cur_seg= """ select c.curso_capacitacion_id, c.cur_cap_nombre, g.grupo_id, g.gru_nombre, p.ponente_id, p.pon_nombre, g.gru_horario
    from grupo g, curso_capacitacion c, ponente p
    where g.ponente_id = p.ponente_id and c.curso_capacitacion_id = g.curso_capacitacion_id and c.cur_cap_estado = :curso_desarrollo; 
    """
    
    try:
        # esta parte imaginamos un poco que CUR_CAP_ESTADO = 1, SON LOS CURSOS EN DESARROLLO
        bind_data = {'curso_desarrollo':"1"}
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
                'gru_hor': row[6]
            })
        return result_dict

    except:   
        return False 

def add_curso_seguimiento(data):

    query_add_cur_seg = """ INSERT INTO grupo(
	ponente_id, gru_nombre, curso_capacitacion_id, gru_estado, gru_fecha_inicio, gru_fecha_final, gru_horario, gru_observaciones)
	VALUES (:pon_id, :gru_nom, :cur_cap_id, :gru_est, :gru_fec_ini, :gru_fec_fin, :gru_hor, :gru_obs); 
    """

    try:

        bind_data = {
            'pon_id': data["pon_id"],
            'gru_nom': data["gru_nom"],
            'cur_cap_id': data["cur_cap_id"],
            'gru_est': data["gru_est"],
            'gru_fec_ini': data["gru_fec_ini"],
            'gru_fec_fin': data["gru_fec_fin"],
            'gru_hor': data["gru_hor"],
            'gru_obs': data["gru_obs"]
        }
        
        db.session.execute(query_add_cur_seg, bind_data)
        db.session.commit()
        return True  
    except:
        return False

def get_docentes_por_curso(id):
    
    query_cur_seg_doc = """ SELECT d.docente_id, d.doc_nombre, d.doc_email 
    FROM lista_participante l, docente d 
    WHERE l.docente_id = d.docente_id and l.grupo_id = :gru_id; 
    """
    
    try:
        
        bind_data = {'gru_id':id}
        result_dict = {"data":[]}

        result = db.session.execute(query_cur_seg_doc, bind_data)
        for row in result:
            result_dict['data'].append({
                'doc_id': row[0],
                'doc_nom': row[1],
                'doc_email': row[2]
            })
        return result_dict
    except:   
        return False 
    

