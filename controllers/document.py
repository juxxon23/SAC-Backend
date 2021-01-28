from flask.views import MethodView
from flask import jsonify, request
from marshmallow import validate
from helpers.document_tool import DocumentTool
from db.mongodb.mongodb_manager import MongoDBManager
from validators.document_val import DocumentVal, DocumentUpdate


doc_tool = DocumentTool()
doc_schema = DocumentVal()
doc_up_schema = DocumentUpdate()
mongo_tool = MongoDBManager()

class Document(MethodView):

    def get(self):
        try:
            id_acta = request.headers.get('id_a')
            if id_acta == None:
                docs = mongo_tool.get_all_docs()
                docs_list = []
                for doc in docs:
                    docs_list.append({
                        '_id': str(doc['_id']),
                        'document_u': doc['document_u'],
                        #'format_id': doc['format_id'],
                        #'content': doc['content']
                    })
                return jsonify({'docs': docs_list})
            else:
                doc_user = mongo_tool.get_by_id(id_acta)
                return jsonify({'user_doc': doc_user['content']}), 200
        except Exception as ex:
            return jsonify({'status':'exception', 'ex': ex}), 400

    def post(self):
        try:
            data = request.get_json()
            errors = doc_schema.validate(data)
            if errors:
                return jsonify({'status':'error', 'errors':errors}), 400
            msg = mongo_tool.add_doc(data)
            template = doc_tool.template_selector(data['format_id'])
            if msg == 'error':
                return jsonify({"status": "add error"}), 400
            else:
                answ = {'id_acta': str(msg), 'document_u': data['document_u'], 'template': template}
                return jsonify({"format": answ, "status": "ok"}), 200     
        except:
            return jsonify({"status":"exception"}), 400
    
    def put(self):
        try:
            data = request.get_json()
            errors = doc_up_schema.validate(data)
            if errors:
                return jsonify({'status':'validation_error', 'errors':errors}), 400
            msg = mongo_tool.update_doc(data['id_acta'], data['document_u'], data['content'])
            if msg == 'ok':
                return jsonify({"status": "ok"}), 200    
            else:
                return jsonify({"status": "update error", "ex": msg}), 400         
        except:
            return jsonify({"status":"exception"}), 400