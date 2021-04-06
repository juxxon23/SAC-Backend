from flask import jsonify, request
from flask.views import MethodView
from app.db.postgresql.postgresql_manager import PostgresqlManager
from app.db.mongodb.mongodb_manager import MongoDBManager
from app.db.postgresql.model import User, RequestEdit

postgres_tool = PostgresqlManager()
mongo_tool = MongoDBManager()

class ReqEdit(MethodView):
    
    def get(self):
        try:
            id_user = request.headers.get('id_u')
            res_docs = postgres_tool.get_all(RequestEdit)
            reqs = {}
            reqs_li = []
            for res in res_docs:
                if id_user == res.creator:
                    doc_u = postgres_tool.get_by_id(User, res.id_u)
                    reqs = {
                        'document_u': doc_u.document_u,
                        'id_a': res.id_a,
                        'id_req': res.id_req
                    }
                    reqs_li.append(reqs)
            return jsonify({'status': 'welcome', 'reqs_edit': reqs_li}), 200
        except Exception as ex:
            return jsonify({'status': 'exception', 'ex': ex}), 403
        

    def post(self):
        try:
            req_edit = request.get_json()
            id_creator = mongo_tool.get_by_num(req_edit['id_a'])
            reqq = RequestEdit(
                creator=id_creator['id_u'],
                id_a=int(req_edit['id_a']),
                id_u=req_edit['id_u']
            )
            msg = postgres_tool.add(reqq)
            if msg == 'ok':
                return jsonify({'status': 'welcome'}), 200
            else:
                return jsonify({'status':'error', 'error': 'exists'}), 400
        except Exception as ex:
            return jsonify({'status': 'exception', 'ex': ex}), 403
        
    def put(self):
        try:
            accept_edit = request.get_json()
            req_acc = postgres_tool.get_by_req(RequestEdit, accept_edit['id_req'])
            doc = mongo_tool.get_by_num(req_acc.id_a)
            doc['opts'][0].append(req_acc.id_u)
            msg = mongo_tool.update_coll(req_acc.id_a, doc['opts'])
            msg = postgres_tool.delete(req_acc)
            return jsonify({'status': 'ok', 'msg': msg}), 200
        except Exception as ex:
            return jsonify({'status': 'exception', 'ex': ex}), 403


    def delete(self):
        try:
            i_req = request.headers.get('i_req')
            req_dec = postgres_tool.get_by_req(RequestEdit, int(i_req))
            msg = postgres_tool.delete(req_dec)
            return jsonify({'status': 'ok', 'msg': msg}), 200
        except Exception as ex:
            return jsonify({'status': 'exception', 'ex': ex}), 403
            