# Se importan las librerias y clases respectivas para hacer el signin
from flask import jsonify, request
from flask.views import MethodView
from marshmallow import validate
from helpers.encrypt_pass import Crypt
from db.postgresql.model import User
from validators.signin_u import RegisterUser, RegisterExtra
from db.postgresql.postgresql_manager import PostgresqlManager

# Se incializan las variables con su respectivo metodo
encrypt = Crypt()
user_schema1 = RegisterUser()
user_schema2 = RegisterExtra()
postgres_tool = PostgresqlManager()

class Signin(MethodView):
    def post(self):
        try:
            user_signin = request.get_json()
            errors = user_schema1.validate(user_signin)
            if errors:
                return jsonify({'state': 'error', 'error': errors}), 403
            document = postgres_tool.get_by(User, user_signin['email_inst'])
            return jsonify({'state': 'ok'}), 203
        except:
            return jsonify({'state': 'error in the form'}), 403



#Se crea la clase SigninExtra
class SigninExtra(MethodView):

    def put(self):
        print(arreglo)
        try:
            users_signinEx = request.get_json()
            errors = user_schema2.validate(users_signinEx)
            if errors:
                return ({'status': 'error', 'error': errors}),403
            return jsonify({'state': 'ok'}),203
        except:
            return jsonify({'status': 'error'}),403

