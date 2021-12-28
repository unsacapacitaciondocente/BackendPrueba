from flask import Flask, request, jsonify, make_response,session
import jwt
import json
from flask_restful import Resource
from datetime import  datetime, timedelta
from functools import wraps
from app import app
from app.models import usuario

app.config['SECRET_KEY'] = 'e4956c1e746a439599292e267b8afa6a'


class Login_api(Resource):
    def get(self):        
        return jsonify({"message":"Solo POST"})

    def post(self):
        data = request.json
        usuario_=usuario.buscar_username(data['username'])
        if usuario is not None and usuario_['password']==data['password']:
            print('aqui si entra')
            session['logged_in'] = True
            token =jwt.encode({
                'user':data['username'],
                'expiration': str(datetime.utcnow()+ timedelta(minutes=2))
            },
            app.config['SECRET_KEY'])
            return jsonify({'token': token,'usuario':data['username'],'id':usuario_['id'],'nombre':usuario_['nombre'],'categoria':'Administrador'})
        else:
            return make_response('Unable to verify',403, {'www-Authenticate': 'Basic real:"Authentication failed"'})

""" def token_required(func):
    @wraps(func)
    def decorated(*args,**kwargs):
        token = request/args.get('token')
        if not token:
            return jsonify({'Alert!':'Token is missing'})
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'Alert':'Invalid token!'})
    return decorated

@app.route('/public')
def public():
    return 'For public'

@app.route('/auth')
@token_required
def auth():
    return 'JWT is verified, welcome to your dashboard'  """


