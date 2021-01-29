import os
from datetime import date, time
from unidecode import unidecode
from pydocx import PyDocX
from helpers.html2text import html2text
from data.document.document_keys import header_keys, body_keys, footer_keys
from data.document.document_keys import headers_colm, body_colm, footer_colm


class DocumentTool():

    """DocumentTool: Manipulacion de documentos 'Actas de compromiso'."""
    __author__ = "Grimpoteuthis (jphenao979@misena.edu.co)"
    __contributors__ = ["Nelson Andres Tique", "natique03@misena.edu.co"]

    # List with document sections - [header, body, footer]
    document_content = {}

    # path: string - docx path
    # outname: string - filename
    def docx_to_html(self, path, outname):
        with open(outname, "w") as file_html:
            html = PyDocX.to_html(path)
            file_html.write(html)
            return html

    # path: string - html path
    def read_html(self, path):
        with open(path, "r") as file_html:
            string_data = file_html.read()
            return string_data

    # html_data : string - html string
    def html_to_text(self, html_data):
        text_data = html2text(html_data)
        split_data = self.del_space(text_data)
        return split_data

    # html_format : string - html path
    def html_to_string(self, html_format):
        html_data = self.read_html(html_format)
        split_html = self.del_space(html_data)
        sep = ''
        split_data = sep.join(split_html)
        return split_data

    # opt : string - template option
    def template_selector(self, opt):
        if opt == 2:
            template = 'data/document/2.txt'
            return template
        else:
            template = 'data/document/1.txt'
            return template

    # data_string : string - data
    def del_space(self, data_string):
        # Split donde exista un salto de linea
        split_data = data_string.split('\n')
        for i in range(len(split_data)):
            # Borra espacios al principio y final de cada string
            split_data[i] = split_data[i].strip()
        return split_data

    # content : string - html data
    def get_content_data(self, content):
        try:
            text_data = self.html_to_text(content)
            header = self.extract_header_data(text_data)
            body_index = header['len_header']
            body = self.extract_body_data_v1(text_data[body_index:len(text_data)])
            footer_index = body_index + body[len(body)-1]
            footer = self.extract_footer_data(
                text_data[footer_index:len(text_data)])
            self.document_content = {
                'header': header,
                'body': body,
                'footer': footer
            }
            return self.document_content
        except Exception as ex:
            print(ex)

    # content : list - html text
    # header_keys : list - dict keys
    def extract_header_data(self, content, header_keys=header_keys):
        header_content = {}
        k = 0
        cont = 0
        for i in range(len(content)):
            header_col = unidecode(content[k].lower())
            if cont == len(headers_colm):
                header_content['len_header'] = k
                return header_content
            elif headers_colm[i] in header_col:
                cont += 1
                header_content[header_keys[i]] = content[k+1]
            k += 2

    # content : list - html text
    def extract_body_data_v1(self, content):
        body_content = []
        cont = 0
        if content[1] == '':
            cont += 1
            content.pop(1)
        for i in range(len(content)):
            if body_colm[len(body_colm)-1] in unidecode(content[i].lower()):
                cont += 2
                body_content.append(content[i])
                body_content.append(content[i+1])
                body_content.append(cont)
                return body_content
            body_content.append(content[i])
            cont += 1

    # content : list - html text
    # body_keys : list - dict keys
    def extract_body_data_v2(self, content, body_keys=body_keys):
        body_content = {}
        cont = 0
        # Elimina el espacio extra generado por el html_to_text
        if content[1] == '':
            content.pop(1)
        for i in range(len(content)):
            # Unicode to ASCII
            body_col = unidecode(content[i].lower())
            if body_colm[i] in body_col and content[i+1] != body_colm[i+1]:
                if body_colm[0] in body_col[i]:
                    cont += 1
                    body_content[body_keys[0]] = content[i+1]
                elif body_colm[5] in body_col[i]:
                    cont += 1
                    body_content[body_keys[2]] = content[i+1]
                    return body_content
                else:
                    # Falta extraccion de instructor junto a sus competencias
                    # y resultados
                    pass

    # content : list - html text
    # footer_keys : list - dict keys
    def extract_footer_data(self, content, footer_keys=footer_keys):
        footer_content = {}
        footer_col = ''
        user = {}
        list_user = []
        cont = 6
        #k = 0
        if footer_colm[0] in unidecode(content[0].lower()):
            content.pop(0)
            if content[0] == '':
                content.pop(0)
        for i in range(len(content)):
            footer_col = unidecode(content[i].lower())
            if footer_colm[1] in footer_col:
                footer_content[footer_keys[i]] = content[i+3]
            elif footer_colm[2] in footer_col:
                footer_content[footer_keys[i]] = content[i+3]
            elif footer_colm[3] in footer_col:
                footer_content[footer_keys[i]] = content[i+3]
                break
        for j in range(4, 7):
            footer_col = unidecode(content[j+1].lower())
            if footer_colm[j] in footer_col:
                footer_content[footer_keys[j-1]] = content[j+1]
        for k in range(7, 14):
            footer_col = unidecode(content[k].lower())
            if footer_colm[k] in footer_col:
                pass
            else:
                pass
        for m in range(14, len(content)):
            user[footer_keys[cont]] = content[m]
            cont += 1
            if cont == 12:
                list_user.append(user)
                user = {}
                cont = 6
        footer_content['list_asis'] = list_user
        return footer_content


#dt = DocumentTool()
#data = dt.read_html('1.txt')
#split_data = dt.html_to_text(data)
#document_content = dt.get_content_data(split_data)
# print(document_content)
