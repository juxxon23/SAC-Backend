from flask.views import MethodView
from flask import jsonify, request
from marshmallow import validate
from app.helpers.document_tool import DocumentTool
from app.db.mongodb.mongodb_manager import MongoDBManager
from app.db.postgresql.postgresql_manager import PostgresqlManager
from app.db.postgresql.model import User
from app.helpers.srch import SearchTool
from app.helpers.error_handler import PostgresqlError

doc_tool = DocumentTool()
mongo_tool = MongoDBManager()
postgres_tool = PostgresqlManager()
schr = SearchTool()
pse = PostgresqlError()


class Search(MethodView):

    def get(self):
        try:
            id_acta = request.headers.get('id_a')
            id_u = request.headers.get('id_u')
            doc_user = mongo_tool.get_by_num(id_acta)
            if doc_user['id_u'] == id_u or id_u in doc_user['opts'][0]:
                template = doc_tool.template_selector(
                    doc_user['format_id'])
                u = doc_user['content']
                html_template = doc_user['html_content']
                return jsonify({'u': u, 'template': template, 'h_temp': html_template}), 200
            else:
                return jsonify({'msg': 'El usuario no tiene permisos de edicion sobre el acta'}), 400
        except Exception as ex:
            return jsonify({'status': 'exception', 'ex': str(ex)}), 400

    def post(self):
        try:
            data = request.get_json()
            # Falta validacion
            opt = data['opt']
            data_opt = data['dataOpt']
            curr_u = data['currUser']
            if opt == "0":
                doc_user = mongo_tool.get_by_num(data_opt)
                if doc_user == None:
                    return jsonify({'status': 'error', 'error': 'not found'}), 400
                document = postgres_tool.get_by_id(User, doc_user['id_u'])
                msg = pse.msg(document)
                if msg.get('status') != 'ok':
                    return jsonify(msg), 400
                content = schr.get_data_option(doc_user, document.document_u, curr_user=curr_u)
                return jsonify({'u': content['u'], 'template': content['template']}), 200
            elif opt == "1":
                doc_u = postgres_tool.get_by(User, data_opt)
                msg = pse.msg(doc_u)
                if msg.get('status') != 'ok':
                    return jsonify(msg), 400
                doc_user = mongo_tool.get_all_docs()
                content = schr.get_all_list(doc_user, opt='check_id', user_pos=doc_u, curr_user=curr_u)
                return jsonify({'u': content}), 200
            elif opt == "2":
                doc_user = mongo_tool.get_all_docs()
                content = schr.get_all_list(doc_user, opt='description', curr_user=curr_u, descript=data_opt)
                return jsonify({'u': content}), 200
            else:
                return jsonify({'status': 'error', 'error': 'invalid option'}), 400
        except Exception as ex:
            return jsonify({'status': 'exception', 'ex': str(ex)}), 400
