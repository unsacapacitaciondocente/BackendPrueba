from flask import Flask, request, jsonify, make_response,session
import jwt
import json
from flask_restful import Resource
from datetime import  datetime, timedelta
from functools import wraps
from app import app
from app.models import ponente

app.config['SECRET_KEY'] = 'e4956c1e746a439599292e267b8afa6a'


class Login_Ponente_api(Resource):
    def get(self):        
        return jsonify({"message":"Solo POST"})

    def post(self):
        data = request.json
        usuario_=ponente.buscar_PonEmail(data['username'])
        if ponente is not None and usuario_['contrasena']==data['password']:
            print('aqui si entra')
            session['logged_in'] = True
            token =jwt.encode({
                'user':data['username'],
                'expiration': str(datetime.utcnow()+ timedelta(minutes=2))
            },
            app.config['SECRET_KEY'])
            return jsonify({'token': token,'usuario':data['username'],'id':usuario_['id'],'nombre':usuario_['nombre'],'categoria':'Ponente'})
        else:
            return make_response('Unable to verify',403, {'www-Authenticate': 'Basic real:"Authentication failed"'})


