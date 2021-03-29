from app.helpers.document_tool import DocumentTool

doc_tool = DocumentTool()


class SearchTool():

    def get_data_option(self, doc_user):
        template = doc_tool.template_selector(
            doc_user['format_id'])
        doc_u = []
        if doc_user.get('content') == None:
            u = {
                'id_a': doc_user['id_a'],
                'id_u': doc_user['id_u'],
                'format_id': doc_tool.template_code(doc_user['format_id']),
            }
        else:
            u = {
                'id_a': doc_user['id_a'],
                'id_u': doc_user['id_u'],
                'format_id': doc_tool.template_code(doc_user['format_id']),
                'content': doc_user['content']
            }
        doc_u.append(u)
        return {'u': doc_u, 'template': template}

    def get_all_list(self, doc_user, opt="no_check", id_u="00"):
        docs_list = []
        if opt == 'no_check':
            for doc in doc_user:
                if doc.get('content') == None:
                    docs_list.append({
                        'id_a': doc['id_a'],
                        'id_u': doc['id_u'],
                        'format_id': doc_tool.template_code(doc_user['format_id']),
                    })
                else:
                    docs_list.append({
                        'id_a': doc['id_a'],
                        'id_u': doc['id_u'],
                        'format_id': doc_tool.template_code(doc_user['format_id']),
                        'content': doc['content']
                    })
        elif opt == 'check_id':
            for doc in doc_user:
                if doc.get('id_u') == id_u:
                    if doc.get('content') == None:
                        docs_list.append({
                            'id_a': doc['id_a'],
                            'id_u': id_u,
                            'format_id': doc_tool.template_code(doc['format_id']),
                        })
                    else:
                        docs_list.append({
                            'id_a': doc['id_a'],
                            'id_u': id_u,
                            'format_id': doc_tool.template_code(doc['format_id']),
                            'content': doc['content']
                        })
        return docs_list
