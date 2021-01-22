from flask.views import MethodView
from flask import jsonify, request
from helpers.document_tool import DocumentTool

doc_tool = DocumentTool()

class Document(MethodView):

    def post(self):
        data = request.get_json()
        print(data)
        template = doc_tool.read_html('data/document/acta_cierre.txt')
        return jsonify({"template": template, "status": "ok"}), 200