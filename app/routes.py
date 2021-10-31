from flask_restful import Api

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

from app.resources.documento_ponente.documento_ponente_api import Documento_ponente_api
from app.resources.documento_ponente.documento_ponente_add_api import Documento_ponente_add_api
from app.resources.documento_ponente.documento_ponente_delete_api import Documento_ponente_delete_api
from app.resources.documento_ponente.documento_ponente_detalle_api import Documento_ponente_detalle_api
from app.resources.documento_ponente.documento_ponente_edit import Documento_ponente_edit_api

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

from app.resources.asistencia_connection.asistencia_lista_curso_ponentes_api import Asistencia_lista_curso_ponentes_api
from app.resources.asistencia_connection.asistencia_historial_asistencia_api import Asistencia_historial_asistencia_api
from app.resources.asistencia_connection.asistencia_registro_asistencia_api import Asistencia_registro_asistencia_api
from app.resources.asistencia_connection.asistencia_calificaciones_ponente_api import Asistencia_calificaciones_ponente_api

from app.resources.curso_seguimiento.curso_seguimiento_api import Curso_seguimiento_api
from app.resources.curso_seguimiento.curso_seguimiento_add_api import Curso_seguimiento_add_api
from app.resources.curso_seguimiento.curso_seguimiento_docentes_api import Curso_seguimiento_docentes_api

from app.resources.certificado.certificado_send_api import Certificado_export

from app.resources.login.login import Login_api

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

api.add_resource(Documento_ponente_api,'/documento_ponente/','/documento_ponente/<string:id>')
api.add_resource(Documento_ponente_add_api,'/documento_ponente/create/','/documento_ponente/create/<string:id>')
api.add_resource(Documento_ponente_edit_api,'/documento_ponente/edit/','/documento_ponente/edit/<string:id>')
api.add_resource(Documento_ponente_delete_api,'/documento_ponente/delete/','/documento_ponente/delete/<string:id>')
api.add_resource(Documento_ponente_detalle_api,'/documento_ponente/detalle/','/documento_ponente/detalle/<string:id>')

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

api.add_resource(Asistencia_lista_curso_ponentes_api,'/asistencia_lista_curso/','/asistencia_lista_curso/<string:id>')
api.add_resource(Asistencia_historial_asistencia_api,'/asistencia_historial/','/asistencia_historial/<string:id>')
api.add_resource(Asistencia_registro_asistencia_api, '/asistencia_registro/','/asistencia_registro/<string:id>' )
api.add_resource(Asistencia_calificaciones_ponente_api, '/asistencia_calificaciones/','/asistencia_calificaciones/<string:id>')

api.add_resource(Curso_seguimiento_api,'/curso_seguimiento/','/curso_seguimiento/<string:id>')
api.add_resource(Curso_seguimiento_add_api, '/curso_seguimiento/create/', '/curso_seguimiento/create/<string:id>')
api.add_resource(Curso_seguimiento_docentes_api,'/curso_seguimiento/docentes/','/curso_seguimiento/docentes/<string:id>')

api.add_resource(Certificado_export,'/certificado_export/','/certificado_export/<string:id>')

api.add_resource(Login_api,'/login/','/login/<string:id>')

api.add_resource(Report, '/report/', '/report/<string:id>')

