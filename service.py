#Libraries
from flask_cors import CORS
from app import app
from app.routes import api
#Configuration 
CORS(app)

if __name__ == '__main__':
    app.run(debug=False)

#from flask import Flask
#from flask_restful import Resource, Api

#app = Flask(__name__)
#api = Api(app)

#class HelloWorld(Resource):
#    def get(self):
#        return {'hello': 'world'}

#api.add_resource(HelloWorld, '/')

#if __name__ == '__main__':
#    app.run(debug=False)






