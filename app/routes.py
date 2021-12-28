from re import I
from flask_restful import Api

from app.resources.curso_seguimiento.curso_seguimiento_add_api import Curso_seguimiento_add_api
from app.resources.curso_seguimiento.curso_seguimiento_delete_api import Curso_seguimiento_delete_api
from app.resources.curso_seguimiento.curso_seguimiento_docentes_api import Curso_seguimiento_docentes_api
from app.resources.curso_seguimiento.curso_seguimiento_edit_api import Curso_seguimiento_edit_api
from app.resources.curso_seguimiento.curso_seguimiento_form_api import Curso_seguimiento_cursos, Curso_seguimiento_ponentes
from app.resources.curso_seguimiento.curso_seguimiento_detalle_api import Curso_seguimiento_detalle_api
from app.resources.curso_seguimiento.curso_seguimiento_matricula import Curso_seguimiento_desmatricular, Curso_seguimiento_matricular, Curso_seguimiento_prematricular, Curso_seguimiento_cambio_estado
from app.resources.curso_seguimiento.curso_seguimiento_prematricula import Curso_seguimiento_lista_prematriculados, Curso_seguimiento_prematriculado

from app.resources.index import Index
from app.resources.curso.curso_api import Curso_api
from app.resources.report import Report
from app.resources.curso.curso_delete_api import Curso_delete_api
from app.resources.curso.curso_edit_api import Curso_edit_api
from app.resources.curso.curso_add_api import Curso_add_api
from app.resources.curso.curso_detalle_api import Curso_detalle_api

from app.resources.ponente.ponente_api import Ponente_api
from app.resources.ponente.ponente_add_api import Ponente_add_api
from app.resources.ponente.ponente_delete_api import Ponente_delete_api
from app.resources.ponente.ponente_detalle_api import Ponente_detalle_api
from app.resources.ponente.ponente_edit_api import Ponente_edit_api

from app.resources.docente.docente_api import Docente_api
from app.resources.docente.docente_add_api import Docente_add_api
from app.resources.docente.docente_delete_api import Docente_delete_api
from app.resources.docente.docente_detalle import Docente_detalle_api
from app.resources.docente.docente_edit_api import Docente_edit_api

from app.resources.resolucion.resolucion_api import Resolucion_api
from app.resources.resolucion.resolucion_add_api import Resolucion_add_api
from app.resources.resolucion.resolucion_delete_api import Resolucion_delete_api
from app.resources.resolucion.resolucion_detalle_api import Resolucion_detalle_api
from app.resources.resolucion.resolucion_edit_api import Resolucion_edit_api

from app.resources.usuario.usuario_api import Usuario_api
from app.resources.usuario.usuario_add_api import Usuario_add_api
from app.resources.usuario.usuario_delete_api import Usuario_delete_api
from app.resources.usuario.usuario_detalle_api import Usuario_detalle_api
from app.resources.usuario.usuario_edit_api import Usuario_edit_api


from app.resources.curso_capacitacion.curso_capacitacion_api import Curso_capacitacion_api
from app.resources.curso_capacitacion.curso_capacitacion_add_api import Curso_capacitacion_add_api
from app.resources.curso_capacitacion.curso_capacitacion_delete_api import Curso_capacitacion_delete_api
from app.resources.curso_capacitacion.curso_capacitacion_detalle_api import Curso_capacitacion_detalle_api
from app.resources.curso_capacitacion.curso_capacitacion_edit_api import Curso_capacitacion_edit_api

from app.resources.grupo.grupo_api import Grupo_api
from app.resources.grupo.grupo_add_api import Grupo_add_api
from app.resources.grupo.grupo_delete_api import Grupo_delete_api
from app.resources.grupo.grupo_detalle_api  import Grupo_detalle_api
from app.resources.grupo.grupo_edit_api import Grupo_edit_api

from app.resources.reportes.cursos_by_ponente_api import Cursos_by_ponente_api



from app.resources.asistencia.asistencia_api import Asistencia_api
from app.resources.asistencia.asistencia_add_api import Asistencia_add_api
from app.resources.asistencia.asistencia_delete_api import Asistencia_delete_api
from app.resources.asistencia.asistencia_detalle_api import Asistencia_detalle_api
from app.resources.asistencia.asistencia_edit_api import Asistencia_edit_api

from app.resources.asistencia_docente.asistencia_docente_api import Asistencia_docente_api
from app.resources.asistencia_docente.asistencia_docente_add_api import Asistencia_docente_add_api
from app.resources.asistencia_docente.asistencia_docente_delete_api import Asistencia_docente_delete_api
from app.resources.asistencia_docente.asistencia_docente_detalle_api import Asistencia_docente_detalle_api
from app.resources.asistencia_docente.asistencia_docente_edit_api import Asistencia_docente_edit_api
from app.resources.asistencia_docente.asistencia_docente_moduloDocente import Asistencia_docente_asistenciaPorFecha
from app.resources.asistencia_docente.asistencia_docente_moduloDocente import Asistencia_docente_asistenciaListCurso
from app.resources.asistencia_docente.asistencia_docente_moduloDocente import Asistencia_docente_historialAsistencia
from app.resources.asistencia_docente.asistencia_docente_moduloDocente import Asistencia_docente_setAsistencia

#from app.resources.asistencia_connection.asistencia_curso_api import Asistencia_curso_api
from app.resources.asistencia_connection.asistencia_lista_curso_ponentes_api import Asistencia_lista_curso_ponentes_api
from app.resources.asistencia_connection.asistencia_historial_asistencia_api import Asistencia_historial_asistencia_api
from app.resources.asistencia_connection.asistencia_registro_asistencia_api import Asistencia_registro_asistencia_api
from app.resources.asistencia_connection.asistencia_calificaciones_ponente_api import Asistencia_calificaciones_ponente_api
from app.resources.asistencia_connection.asistencia_editar_calificacion_api import Asistencia_editar_calificacion_api
from app.resources.asistencia_connection.asistencia_editar_asistencia_api import Asistencia_editar_asistencia_api
from app.resources.asistencia_connection.asistencia_guardar_registro_asistencia_api import Asistencia_guardar_registro_asistencia_api

from app.resources.lista_participante.lista_participante_add_api     import Lista_participante_add_api
from app.resources.lista_participante.lista_participante_edit_api import Lista_participante_edit_api


from app.resources.convocatoria.convocatoria_api import Convocatoria_api
from app.resources.convocatoria.convocatoria_registro_preinscrito_api import Convocatoria_registro_preinscrito_api

from app.resources.curso_seguimiento.curso_seguimiento_api import Curso_seguimiento_api


from app.resources.certificado.certificado_all_api import Certificado_all_api
from app.resources.certificado.certificado_detalle_api import Certificado_detalle_api
from app.resources.certificado.certificado_generate_docentes_api import Certificado_generate_docentes_api
from app.resources.certificado.certificado_delete_api import Certificado_delete_api
from app.resources.certificado.certificado_increment_api import Certificado_increment_api

from app.resources.correos.correo_convocatoria_api import Correo_convocatoria_api

from app.resources.login.login import Login_api
from app.resources.login.loginDocente import Login_Docente_api
from app.resources.login.loginPonente import Login_Ponente_api

from app import app
#Api
api = Api(app)
#Routes
api.add_resource(Index, '/', '/<string:id>')

api.add_resource(Curso_api, '/curso/', '/curso/<int:id>')
api.add_resource(Curso_add_api, '/curso/create/', '/curso/create/<string:id>' )
api.add_resource(Curso_edit_api, '/curso/edit/', '/curso/edit/<string:id>')
api.add_resource(Curso_delete_api, '/curso/delete/', '/curso/delete/<string:id>')
api.add_resource(Curso_detalle_api, '/curso/detalle/', '/curso/detalle/<string:id>' )

api.add_resource(Ponente_api,'/ponente/','/ponente/<string:id>')
api.add_resource(Ponente_add_api,'/ponente/create/','/ponente/create/<string:id>')
api.add_resource(Ponente_edit_api,'/ponente/edit/','/ponente/edit/<string:id>')
api.add_resource(Ponente_delete_api,'/ponente/delete/','/ponente/delete/<string:id>')
api.add_resource(Ponente_detalle_api,'/ponente/detalle/','/ponente/detalle/<string:id>')

api.add_resource(Docente_api,'/docente/','/docente/<string:id>')
api.add_resource(Docente_add_api,'/docente/create/','/docente/create/<string:id>')
api.add_resource(Docente_edit_api,'/docente/edit/','/docente/edit/<string:id>')
api.add_resource(Docente_delete_api,'/docente/delete/','/docente/delete/<string:id>')
api.add_resource(Docente_detalle_api,'/docente/detalle/','/docente/detalle/<string:id>')

api.add_resource(Resolucion_api, '/resolucion/','/resolucion/<string:id>')
api.add_resource(Resolucion_add_api, '/resolucion/create/','/resolucion/create/<string:id>')
api.add_resource(Resolucion_edit_api, '/resolucion/edit/','/resolucion/edit/<string:id>')
api.add_resource(Resolucion_delete_api, '/resolucion/delete/','/resolucion/delete/<string:id>')
api.add_resource(Resolucion_detalle_api, '/resolucion/detalle/','/resolucion/detalle/<string:id>')

api.add_resource(Usuario_api, '/usuario/','/usuario/<string:id>')
api.add_resource(Usuario_add_api, '/usuario/create/','/usuario/create/<string:id>')
api.add_resource(Usuario_edit_api, '/usuario/edit/','/usuario/edit/<string:id>')
api.add_resource(Usuario_delete_api, '/usuario/delete/','/usuario/delete/<string:id>')
api.add_resource(Usuario_detalle_api, '/usuario/detalle/','/usuario/detalle/<string:id>')


api.add_resource(Curso_capacitacion_api,'/curso_capacitacion/','/curso_capacitacion/<string:id>')
api.add_resource(Curso_capacitacion_add_api,'/curso_capacitacion/create/','/curso_capacitacion/create/<string:id>')
api.add_resource(Curso_capacitacion_edit_api,'/curso_capacitacion/edit/','/curso_capacitacion/edit/<string:id>')
api.add_resource(Curso_capacitacion_delete_api,'/curso_capacitacion/delete/','/curso_capacitacion/delete/<string:id>')
api.add_resource(Curso_capacitacion_detalle_api,'/curso_capacitacion/detalle/','/curso_capacitacion/detalle/<string:id>')

api.add_resource(Grupo_api,'/grupo/','/grupo/<string:id>')
api.add_resource(Grupo_add_api,'/grupo/create/','/grupo/create/<string:id>')
api.add_resource(Grupo_edit_api,'/grupo/edit/','/grupo/edit/<string:id>')
api.add_resource(Grupo_delete_api,'/grupo/delete/','/grupo/delete/<string:id>')
api.add_resource(Grupo_detalle_api,'/grupo/detalle/','/grupo/detalle/<string:id>')

api.add_resource(Cursos_by_ponente_api,'/reporte/cursoP/','/reporte/cursoP/<string:id>')


api.add_resource(Asistencia_api,'/asistencia/','/asistencia/<string:id>')
api.add_resource(Asistencia_add_api,'/asistencia/create/','/asistencia/create/<string:id>')
api.add_resource(Asistencia_edit_api,'/asistencia/edit/','/asistencia/edit/<string:id>')
api.add_resource(Asistencia_delete_api,'/asistencia/delete/','/asistencia/delete/<string:id>')
api.add_resource(Asistencia_detalle_api,'/asistencia/detalle/','/asistencia/detalle/<string:id>')

api.add_resource(Asistencia_docente_api,'/asistencia_docente/','/asistencia_docente/<string:id>')
api.add_resource(Asistencia_docente_add_api,'/asistencia_docente/create/','/asistencia_docente/create/<string:id>')
api.add_resource(Asistencia_docente_edit_api,'/asistencia_docente/edit/','/asistencia_docente/edit/<string:id>')
api.add_resource(Asistencia_docente_delete_api,'/asistencia_docente/delete/','/asistencia_docente/delete/<string:id>')
api.add_resource(Asistencia_docente_detalle_api,'/asistencia_docente/detalle/','/asistencia_docente/detalle/<string:id>')
api.add_resource(Asistencia_docente_asistenciaPorFecha,'/crearAsistencia/','/crearAsistencia/<string:id>')
api.add_resource(Asistencia_docente_asistenciaListCurso,'/asistencia_lista_curso_docente/','/asistencia_lista_curso_docente/<string:id>')
api.add_resource(Asistencia_docente_historialAsistencia,'/asistencia_historial_docente/','/asistencia_historial_docente/<string:id>')
api.add_resource(Asistencia_docente_setAsistencia,'/marcarAsistencia/','/marcarAsistencia/<string:id>')

#api.add_resource(Asistencia_curso_api,'/asistencia_curso/','/asistencia_curso/<string:id>')
api.add_resource(Asistencia_lista_curso_ponentes_api,'/asistencia_lista_curso/','/asistencia_lista_curso/<string:id>')
api.add_resource(Asistencia_historial_asistencia_api,'/asistencia_historial/','/asistencia_historial/<string:id>')
api.add_resource(Asistencia_registro_asistencia_api,'/asistencia_registro/','/asistencia_registro/<string:id>' )
api.add_resource(Asistencia_calificaciones_ponente_api,'/asistencia_calificaciones/','/asistencia_calificaciones/<string:id>')
api.add_resource(Asistencia_editar_calificacion_api,'/asistencia_editar/','/asistencia_editar/<string:id>')
api.add_resource(Asistencia_editar_asistencia_api,'/asistencia_editasistencia/','/asistencia_editasistencia/<string:id>')
api.add_resource(Asistencia_guardar_registro_asistencia_api,'/guardar_registros_asistencia/','/guardar_registros_asistencia/<string:id>')

api.add_resource(Curso_seguimiento_api,'/curso_seguimiento/','/curso_seguimiento/<string:id>')
api.add_resource(Curso_seguimiento_add_api, '/curso_seguimiento/create/', '/curso_seguimiento/create/<string:id>')
api.add_resource(Curso_seguimiento_docentes_api,'/curso_seguimiento/docentes/','/curso_seguimiento/docentes/<string:id>')
api.add_resource(Curso_seguimiento_delete_api, '/curso_seguimiento/delete/', '/curso_seguimiento/delete/<string:id>')
api.add_resource(Curso_seguimiento_edit_api, '/curso_seguimiento/edit/', '/curso_seguimiento/edit/<string:id>')
api.add_resource(Curso_seguimiento_cursos, '/curso_seguimiento/cursos/', '/curso_seguimiento/cursos/<string:id>' )
api.add_resource(Curso_seguimiento_ponentes, '/curso_seguimiento/ponentes/', '/curso_seguimiento/ponentes/<string:id>' )
api.add_resource(Curso_seguimiento_detalle_api, '/curso_seguimiento/detalle','/curso_seguimiento/detalle/<string:id>')
# no se usa ahora
# api.add_resource(Curso_seguimiento_matricular, '/curso_seguimiento/matricular/', '/curso_seguimiento/matricular/<string:id>')
api.add_resource(Curso_seguimiento_desmatricular, '/curso_seguimiento/desmatricular/', '/curso_seguimiento/desmatricular/<string:id>')
api.add_resource(Curso_seguimiento_prematricular, '/curso_seguimiento/prematricular/', '/curso_seguimiento/prematricular/<string:id>')
api.add_resource(Curso_seguimiento_cambio_estado, '/curso_seguimiento/cambiaEstado/', '/curso_seguimiento/cambiaEstado/<string:id>')
api.add_resource(Curso_seguimiento_lista_prematriculados,'/curso_seguimiento/lista_prematriculados/','/curso_seguimiento/lista_prematriculados/<string:id>')
api.add_resource(Curso_seguimiento_prematriculado,'/curso_seguimiento/prematriculado','/curso_seguimiento/prematriculado/<string:id>')

api.add_resource(Lista_participante_add_api,'/lista_participante/create/','/lista_participante/create/<string:id>')
api.add_resource(Lista_participante_edit_api,'/lista_participante_editar/','/lista_participante_editar/<string:id>')

api.add_resource(Convocatoria_api,'/cursos-convocatoria/','/cursos-convocatoria/<string:id>')
api.add_resource(Convocatoria_registro_preinscrito_api,'/cursos-convocatoria/preinscrito/','/cursos-convocatoria/preinscrito/<string:id>')

api.add_resource(Certificado_all_api,'/certificado/all/','/certificado/all/<string:id>')
api.add_resource(Certificado_detalle_api ,'/certificado/export_local/','/certificado/export_local/<string:id>')
api.add_resource(Certificado_generate_docentes_api ,'/certificado/generate_docente/','/certificado/generate_docente/<string:id>')
api.add_resource(Certificado_delete_api, '/certificado/delete/','/certificado/delete/<string:id>' )
api.add_resource(Certificado_increment_api,'/certificado/increment/','/certificado/increment/<string:id>')



api.add_resource(Login_api,'/login/','/login/<string:id>')
api.add_resource(Login_Docente_api,'/loginDocente/','/loginDocente/<string:id>')
api.add_resource(Login_Ponente_api,'/loginPonente/','/loginPonente/<string:id>')

api.add_resource(Report, '/report/', '/report/<string:id>')

api.add_resource(Correo_convocatoria_api, '/correo/send/', '/correo/send/<string:id>' )