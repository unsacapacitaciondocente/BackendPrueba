from flask import Flask, request, jsonify, make_response,session
import jwt
import json
from flask_restful import Resource
from datetime import  datetime, timedelta
from functools import wraps
from app import app
from app.models import docente

app.config['SECRET_KEY'] = 'e4956c1e746a439599292e267b8afa6a'


class Login_Docente_api(Resource):
    def get(self):        
        return jsonify({"message":"Solo POST"})

    def post(self):
        data = request.json
        docente_=docente.buscar_docEmail(data['username'])
        if docente is not None and docente_['dni']==data['password']:
            print('aqui si entra')
            session['logged_in'] = True
            token =jwt.encode({
                'user':data['username'],
                'expiration': str(datetime.utcnow()+ timedelta(minutes=2))
            },
            app.config['SECRET_KEY'])
            return jsonify({'token': token,'usuario':data['username'],'id':docente_['id'],'nombre':docente_['nombre'],'categoria':'Docente'})
        else:
            return make_response('Unable to verify',403, {'www-Authenticate': 'Basic real:"Authentication failed"'})


