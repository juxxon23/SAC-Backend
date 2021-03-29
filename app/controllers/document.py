from flask.views import MethodView
from flask import jsonify, request
from marshmallow import validate
from app.helpers.document_tool import DocumentTool
from app.helpers.srch import SearchTool
from app.db.mongodb.mongodb_manager import MongoDBManager
from app.validators.document_val import DocumentVal, DocumentUpdate, CollaboratorShare
from app.db.postgresql.postgresql_manager import PostgresqlManager
from app.db.postgresql.model import User, InfoStats
from app.helpers.error_handler import PostgresqlError

doc_tool = DocumentTool()
doc_schema = DocumentVal()
doc_up_schema = DocumentUpdate()
mongo_tool = MongoDBManager()
postgres_tool = PostgresqlManager()
share_schema = CollaboratorShare()
schr = SearchTool()
pse = PostgresqlError()


class Document(MethodView):

    def get(self):
        try:
            id_u = request.headers.get('id_u')
            doc_u = postgres_tool.get_by_id(User, id_u)
            msg = pse.msg(doc_u)
            if msg.get('status') != 'ok':
                return jsonify(msg), 400
            docs = mongo_tool.get_all_docs()
            docs_list = schr.get_all_list(docs, opt='check_id', id_u=doc_u)
            return jsonify({'docs': docs_list}), 200
        except Exception as ex:
            return jsonify({'status': 'exception', 'ex': str(ex)}), 400

    def post(self):
        try:
            data = request.get_json()
            errors = doc_schema.validate(data)
            if errors:
                return jsonify({'status': 'error', 'errors': errors}), 400
            curr_a = postgres_tool.get_num_act(InfoStats, 'curr_act')
            curr_a.value_info += 1
            data['id_a'] = curr_a.value_info
            msg = mongo_tool.add_doc(data)
            if msg == 'error':
                return jsonify({"status": "add error"}), 400
            else:
                msg = postgres_tool.update()
                user_cred = postgres_tool.get_by_id(User, data['id_u'])
                if user_cred == None or type(user_cred) == dict:
                    user_cred = 'no-data'
                u = {
                    'document': user_cred.document_u,
                    'email': user_cred.email_inst,
                    'name': user_cred.name_u,
                    'lastname': user_cred.lastname_u,
                    'phone': user_cred.phone_u,
                    'city': user_cred.city_u,
                    'regional': user_cred.regional_u,
                    'center': user_cred.center_u,
                    'bonding': user_cred.bonding_type
                }
                template = doc_tool.template_selector(data['format_id'])
                answ = {'id_acta': data['id_a'], 'us': u, 'template': template}
                return jsonify({"format": answ, "status": "ok"}), 200
        except Exception as ex:
            return jsonify({"status": "exception", "ex": str(ex)}), 400

    def put(self):
        try:
            data = request.get_json()
            errors = doc_up_schema.validate(data)
            if errors:
                return jsonify({'status': 'validation_error', 'errors': errors}), 400
            msg = mongo_tool.update_doc(
                data['id_a'], data['content'])
            if msg == 'ok':
                return jsonify({"status": "ok"}), 200
            else:
                return jsonify({"status": "update error", "ex": msg}), 400
        except Exception as ex:
            return jsonify({"status": "exception", "ex": str(ex)}), 400
