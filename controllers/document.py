from flask.views import MethodView
from flask import jsonify, request
from marshmallow import validate
from helpers.document_tool import DocumentTool
from validators.document_val import DocumentVal
from db.mongodb.mongodb_manager import MongoDBManager

doc_tool = DocumentTool()
doc_schema = DocumentVal()
mongo_tool = MongoDBManager()

class Document(MethodView):

    def get(self):
        pass

    def post(self):
        try:
            data = request.get_json()
            errors = doc_schema.validate(data)
            if errors:
                return jsonify({'status':'error', 'errors':errors}), 400
            # Se agrega el formato al documento que sera guardado en mongodb
            template = doc_tool.read_html('data/document/acta_cierre.txt')
            data['content'] = template
            msg = mongo_tool.add_doc(data)
            if msg == 'error':
                return jsonify({"status": "add error"}), 400
            else:
                answ = {'id_acta': str(msg), 'document_u': data['document_u'], 'template': data['content']}
                return jsonify({"template": answ, "status": "ok"}), 200     
        except:
            return jsonify({"status":"exception"}), 400
    
    def put(self):
        pass