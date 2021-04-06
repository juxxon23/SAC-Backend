from app.helpers.document_tool import DocumentTool
from app.db.postgresql.postgresql_manager import PostgresqlManager
from app.db.postgresql.model import User

doc_tool = DocumentTool()
postgres_tool = PostgresqlManager()


class SearchTool():

    def get_data_option(self, doc_user, document, curr_user=None):
        template = doc_tool.template_selector(
            doc_user['format_id'])
        doc_u = []
        if curr_user is not None:
            u = {}
            if curr_user == doc_user['id_u'] or curr_user in doc_user['opts'][0]:
                u = {
                    'id_a': doc_user['id_a'],
                    'id_u': document,
                    'format_id': doc_tool.template_code(doc_user['format_id']),
                    'description': doc_user['description'],
                    'edit': True
                }
            else:
                u = {
                    'id_a': doc_user['id_a'],
                    'id_u': document,
                    'format_id': doc_tool.template_code(doc_user['format_id']),
                    'description': doc_user['description'],
                    'edit': False
                }
            doc_u.append(u)
        return {'u': doc_u, 'template': template}

    def get_all_list(self, doc_user, opt="no_check", user_pos=None, curr_user=None, descript=None):
        docs_list = []
        if opt == 'no_check':
            for doc in doc_user:
                docs_list.append({
                    'id_a': doc['id_a'],
                    'id_u': user_pos.document_u,
                    'format_id': doc_tool.template_code(doc_user['format_id']),
                    'description': doc['description']
                })
        elif opt == 'check_id':
            for doc in doc_user:
                if doc.get('id_u') == user_pos.id_u:
                    if curr_user is not None:
                        if curr_user == user_pos.id_u or curr_user in doc['opts'][0]:
                            docs_list.append({
                                'id_a': doc['id_a'],
                                'id_u': user_pos.document_u,
                                'format_id': doc_tool.template_code(doc['format_id']),
                                'description': doc['description'],
                                'edit': True
                            })
                        else:
                            docs_list.append({
                                'id_a': doc['id_a'],
                                'id_u': user_pos.document_u,
                                'format_id': doc_tool.template_code(doc['format_id']),
                                'description': doc['description'],
                                'edit': False
                            })
                    else:
                        docs_list.append({
                            'id_a': doc['id_a'],
                            'id_u': user_pos.document_u,
                            'format_id': doc_tool.template_code(doc['format_id']),
                            'description': doc['description']
                        })
        elif opt == 'description':
            for doc in doc_user:
                if curr_user is not None:
                    if descript.lower() in doc['description'].lower():
                        docu = postgres_tool.get_by_id(User, doc['id_u'])
                        if curr_user == doc['id_u'] or curr_user in doc['opts'][0]:
                            docs_list.append({
                                'id_a': doc['id_a'],
                                'id_u': docu.document_u,
                                'format_id': doc_tool.template_code(doc['format_id']),
                                'description': doc['description'],
                                'edit': True
                            })
                        else:
                            docs_list.append({
                                'id_a': doc['id_a'],
                                'id_u': docu.document_u,
                                'format_id': doc_tool.template_code(doc['format_id']),
                                'description': doc['description'],
                                'edit': False
                            })
        return docs_list
