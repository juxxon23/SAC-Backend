from flask import jsonify, request
from flask.views import MethodView
from validators.user_val import LoginUser
from data.config_key import KEY_TOKEN_AUTH
from db.postgresql.model import User, Competencies
from db.postgresql.postgresql_manager import PostgresqlManager
import bcrypt
import jwt
import datetime

user_schema = LoginUser()
postgres_tool = PostgresqlManager()


class Login(MethodView):

    def post(self):
        user_login = request.get_json()
        errors = user_schema.validate(user_login)
        if errors:
            return jsonify({'state': 'Error in validators', 'error': errors})
        pass_ex = user_login['password_u'].encode('utf-8')
        document_cp = postgres_tool.get_by(User, user_login['document_u'])
        if document_cp != None:
            if bcrypt.checkpw(pass_ex, document_cp.password_u.encode('utf-8')):
                encoded_jwt = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(
                    seconds=300), 'nombre': document_cp.name_u}, KEY_TOKEN_AUTH, algorithm='HS256')
                return jsonify({'state': 'welcome', 'token': encoded_jwt}), 203
            else:
                return jsonify({'state': 'password'}), 403
        else:
            return jsonify({'state': 'document'}), 403
        return 'Welcome'
