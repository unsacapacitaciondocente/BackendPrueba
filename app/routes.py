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

api.add_resource(Login_api,'/login/','/login/<string:id>')

api.add_resource(Report, '/report/', '/report/<string:id>')

