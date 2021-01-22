from flask.views import MethodView
from flask import jsonify, request
from marshmallow import validate
from helpers.document_tool import DocumentTool
from validators.document_val import DocumentVal

doc_tool = DocumentTool()
doc_schema = DocumentVal()

class Document(MethodView):

    def post(self):
        try:
            data = request.get_json()
            errors = doc_schema.validate(data)
            if errors:
                return jsonify({'status':'error', 'errors':errors}), 400
            template = doc_tool.read_html('data/document/acta_cierre.txt')
            return jsonify({"template": template, "status": "ok"}), 200
        except:
            return jsonify({"status":"error"}), 400