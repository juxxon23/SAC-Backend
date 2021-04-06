from marshmallow import validate
from flask.views import MethodView
from flask import jsonify, request
from app.helpers.encrypt_pass import Crypt
from app.helpers.error_handler import PostgresqlError
from app.validators.user_val import RegisterUser, RegisterExtra
from app.db.postgresql.model import User
from app.db.postgresql.postgresql_manager import PostgresqlManager
import secrets
import os
from app.helpers.create_user_folder import FileSystemManager
from app.helpers.editprofile_myprofile import EdipMiProfile, MyPerfile
<<<<<<< HEAD
from app.helpers.email_confimation import EmailConfirmation
# Se incializan las variables con su respectivo metodo
=======


>>>>>>> 44fa65561d129149969d77a951a73d48327b0671
encrypt = Crypt()
user_schema = RegisterUser()
edit_schema = RegisterExtra()
postgres_tool = PostgresqlManager()
pse = PostgresqlError()
fsm = FileSystemManager()
emp1 = EdipMiProfile()
emp2 = MyPerfile()
<<<<<<< HEAD
sends_emails = EmailConfirmation()
=======

>>>>>>> 44fa65561d129149969d77a951a73d48327b0671

class Signin(MethodView):

    def post(self):
        try:
            user_signin = request.get_json()
            errors = user_schema.validate(user_signin)
            if errors:
                return jsonify({'status': 'validators', 'error': errors}), 403
            sac_user = postgres_tool.get_by(User, user_signin['document_u'])
            msg = pse.msg(sac_user)
            if msg.get('status') == 'user':
                new_user = User(
                    document_u=user_signin['document_u'],
                    id_u=secrets.token_hex(5),
                    email_inst=user_signin['email_inst'],
                    password_u=encrypt.hash_string(user_signin['password_u']),
                    name_u='',
                    lastname_u='',
                    phone_u='',
                    city_u='',
                    regional_u='',
                    center_u='',
                    bonding_type=3,
                )
                state = postgres_tool.add(new_user)
                msg = pse.msg(state)
                if msg.get('status') == 'ok':
                    sends_emails.send_email(new_user.email_inst)
                    fsm.users_folder(new_user.id_u)
                    return jsonify({'status': 'ok', 'id_u': str(new_user.id_u)}), 200
                else:
                    return jsonify(msg), 400
            else:
                return jsonify(msg), 400
        except Exception as ex:
            return jsonify({'status': 'exception', 'ex': str(ex)}), 403

    def put(self):
        try:
            perfile = request.get_json()
            if perfile.get('password_u') != None:
                if list(perfile.keys())[list(perfile.values()).index(perfile['password_u'])]:
                    for i in perfile:
                        tamaño = len(perfile[i])
                        if tamaño == 0 or int(len(perfile['password_u']) < 0):
                            sac_user = postgres_tool.get_by_id(
                                User, perfile['id_u'])
                            msg = pse.msg(sac_user)
                            if msg.get('status') != 'ok':
                                return jsonify(msg), 400
                            emp2.my_perfile_void(sac_user, perfile)
                            if perfile.get('bonding_type') == "":
                                sac_user.bonding_type = 3
                            else:
                                sac_user.bonding_type = perfile['bonding_type']
                            state = postgres_tool.update()
                            msg = pse.msg(state)
                            if msg.get('status') != 'ok':
                                return jsonify(msg), 400
                            else:
                                return jsonify({'status': 'ok'}), 200
                    errors = edit_schema.validate(perfile)
                    if errors:
                        return jsonify({'status': 'validators', 'error': errors}), 403
                    sac_user = postgres_tool.get_by_id(
                        User, perfile['id_u'])
                    msg = pse.msg(sac_user)
                    if msg.get('status') != 'ok':
                        return jsonify(msg), 400
                    emp2.my_perfile(sac_user, perfile)
                    state = postgres_tool.update()
                    msg = pse.msg(state)
                    if msg.get('status') != 'ok':
                        return jsonify(msg), 400
                    else:
                        return jsonify({'status': 'ok'}), 200
            else:
                for i in perfile:
                    tamaño = len(perfile[i])
                    if tamaño == 0:
                        sac_user = postgres_tool.get_by_id(
                            User, perfile['id_u'])
                        msg = pse.msg(sac_user)
                        if msg.get('status') != 'ok':
                            return jsonify(msg), 400
                        emp1.edit_mi_profile(sac_user, perfile)
                        state = postgres_tool.update()
                        msg = pse.msg(state)
                        if msg.get('status') != 'ok':
                            return jsonify(msg), 400
                        else:
                            return jsonify({'status': 'ok'}), 200
                errors = edit_schema.validate(perfile)
                if errors:
                    return jsonify({'status': 'validators', 'error': errors}), 403
                sac_user = postgres_tool.get_by_id(
                    User, perfile['id_u'])
                msg = pse.msg(sac_user)
                if msg.get('status') != 'ok':
                    return jsonify(msg), 400
                emp1.edit_mi_profile(sac_user, perfile)
                state = postgres_tool.update()
                msg = pse.msg(state)
                if msg.get('status') != 'ok':
                    return jsonify(msg), 400
                else:
                    return jsonify({'status': 'ok'}), 200
        except Exception as e:
            return jsonify({'status': 'exception', 'ex': e}), 400

    def get(self):
        try:
            id_u = request.headers.get('id_u')
            data_user = postgres_tool.get_data_user(User, id_u)
            msg = pse.msg(data_user)
            if msg.get('status') != 'ok':
                return jsonify(msg), 400
            for i in data_user:
                lista=i.name_u, i.lastname_u, i.phone_u, i.bonding_type, i.regional_u, i.center_u, i.city_u
                return jsonify({'data': lista}), 200
        except Exception as ex:
            return jsonify({'status': 'exception', 'ex': str(ex)}), 400
