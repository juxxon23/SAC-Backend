# Se importan las librerias y clases respectivas para hacer el signin
from flask import jsonify, request
from flask.views import MethodView
from marshmallow import validate
from helpers.encrypt_pass import Crypt
from db.postgresql.model import Signin
from validators.signin_u import RegisterUser, RegisterExtra

# Se incializan las variables con su respectivo metodo
encrypt = Crypt()
user_schema1 = RegisterUser()
user_schema2 = RegisterExtra()

# Se crea la variable arreglo la cual tendra un rol el cual es base de datos.
arreglo = [{'email_inst':'nelson@misena.edu.co', 'document_u': '1094972663', 'password_u': 'password1','name_u':'Nelson Andres', 'lastname_u': 'Tique Morales', 'phone_u': '3142184354', 'regional_u': 'Quindio', 'centro_u':'centro de comercio y turismo', 'competencies_u': 'python', 'results_u': 'python basico', 'bonding_type': 'planta'}]
tamaño = len(arreglo)

# Se crea la clase Signin
class Signin(MethodView):

    def post(self):
        try:
            users_signin = request.get_json()
            errors = user_schema1.validate(users_signin)
            if errors:
                return jsonify({'state': 'error', 'error': errors}), 403
            for i in range(tamaño):
                if users_signin['email_inst'] == arreglo[i]['email_inst'] or users_signin['document_u'] == arreglo[i]['document_u']:
                    return jsonify({'state':'existe'})
            else:
                users_signin['password_u'] = encrypt.hash_string(users_signin['password_u'])
                state = arreglo.append(users_signin)
                print('successfully registered')
                return jsonify({'state': 'ok'}), 203
        except:
            print('Error in the form')
            return jsonify({'state': 'error'}), 403

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

