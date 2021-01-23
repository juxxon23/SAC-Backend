from flask_pymongo import PyMongo

mongo = PyMongo()

class MongoDBManager():

    def add_doc(self, doc_data):
        try:
            id_doc = mongo.db.documents.insert(doc_data)
            return id_doc
        except:
            return 'error'

    def delete_doc(self):
        pass

    def update_doc(self):
        pass

    def get_all_docs(self):
        pass

    def get_by_doc(self):
        pass