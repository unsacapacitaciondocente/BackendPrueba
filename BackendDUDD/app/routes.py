from flask_restful import Api

from app.resources.index import Index
from app.resources.curso_api import Curso_api
from app.resources.report import Report
from app.resources.curso_delete_api import Curso_delete_api
from app.resources.curso_edit_api import Curso_edit_api
from app.resources.curso_add_api import Curso_add_api
from app.resources.curso_detalle_api import Curso_detalle_api

from app import app
#Api
api = Api(app)
#Routes
api.add_resource(Index, '/', '/<string:id>')
api.add_resource(Curso_api, '/curso/', '/curso/<string:id>')
api.add_resource(Curso_add_api, '/curso/create/', '/curso/create/<string:id>' )
api.add_resource(Curso_edit_api, '/curso/edit/', '/curso/edit/<string:id>')
api.add_resource(Curso_delete_api, '/curso/delete/', '/curso/delete/<string:id>')
api.add_resource(Curso_detalle_api, '/curso/detalle/', '/curso/detalle/<string:id>' )
api.add_resource(Report, '/report/', '/report/<string:id>')