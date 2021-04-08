from flask import jsonify, request
from flask.views import MethodView
from werkzeug.utils import secure_filename
from random import randint
from app.helpers.create_user_folder import FileSystemManager

fs = FileSystemManager()

class Upfiles(MethodView):
    
    def post(self):
        try:
            id_u = request.headers.get('id_u')
            id_a = request.headers.get('id_a')
            f = request.get_data()
            n = 'app/data/users/{}/{}/data-{}'.format(id_u, id_a, randint(0, 1000))
            with open(n, "wb") as fi:
                fi.write(f)
            return jsonify({'status': 'ok'}), 200
        except Exception as ex:
            return jsonify({'status': 'exception', 'ex': ex}), 403
        
    