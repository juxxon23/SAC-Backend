from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import dumps

mongo = PyMongo()

class MongoDBManager():


    def add_doc(self, doc_data):
        try:
            id_doc = mongo.db.documents.insert(doc_data)
            return id_doc
        except Exception as ex:
            error_msg = {'error': 'error mongodb_tool add_doc', 'ex': ex}
            return error_msg


    def delete_doc(self, id_acta):
        try:
            mongo.db.documents.delete_one({'_id':  ObjectId(id_acta)})
            return 'ok'
        except Exception as ex:
            error_msg = {'error': 'error mongodb_tool delete_doc', 'ex': ex}
            return error_msg


    def update_doc(self, id_acta, doc, cont):
        try:
            up_doc = mongo.db.documents.update_one(
                {'_id':  ObjectId(id_acta)},
                {'$set':{'document_u': doc, 'content': cont}}
                )
            return 'ok'
        except Exception as ex:
            error_msg = {'error': 'error mongodb_tool update_doc', 'ex': ex}
            return error_msg


    def get_all_docs(self):
        try:
            docs = mongo.db.documents.find()
            #docs_d = dumps(docs)
            return docs
        except Exception as ex:
            error_msg = {'error': 'error mongodb_tool get_all_docs', 'ex': ex}
            return error_msg


    def get_by_id(self, id_acta):
        try:
            doc = mongo.db.documents.find_one({'_id': ObjectId(id_acta)})
            return doc
        except Exception as ex:
            error_msg = {'error': 'error mongodb_tool get_by_id', 'ex': ex}
            return error_msg