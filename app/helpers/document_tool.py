import os
import datetime
from unidecode import unidecode
from pydocx import PyDocX
from app.helpers.html2text import html2text
from app.data.document.template.keys.k2020 import header_keys, body_keys, footer_keys
from app.data.document.template.keys.k2020 import headers_colm, body_colm, footer_colm
from app.data.document.template.model.m2021 import content_21


class DocumentTool():

    # Dict with document sections - {header, body_h, body_t, footer}
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
        # html to plain text with markdown format
        text_data = html2text(html_data)
        split_data = self.del_space(text_data)
        split_data[0] = split_data[0] + split_data[1]
        del split_data[1]
        # index list of '' elements
        index_space = []
        for s in range(len(split_data)):
            if split_data[s] == '':
                index_space.append(s)
        index_space = sorted(index_space, reverse=True)
        for d in index_space:
            del split_data[d]
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
        template = ''
        if opt == 1:
            template = 'app/data/document/template/string/2020.txt'
        elif opt == 2:
            template = 'app/data/document/template/string/2021.txt'
        template = self.read_html(template)
        return template

    def template_code(self, opt):
        if opt == 2:
            return 'GD-F-007 V03'
        else:
            return 'GD-F-007 V02'

    # data_string : string - data
    def del_space(self, data_string):
        # Split with '\n'
        split_data = data_string.split('\n')
        for i in range(len(split_data)):
            # Delete spaces at the beginning and end of each string
            split_data[i] = split_data[i].strip()
        return split_data

    def set_content_data(self, id_a, format_id, user_sac):
        try:
            if format_id == 2:
                content_21[0][0] = "ACTA No. {}".format(id_a)
                created_date = datetime.datetime.utcnow()
                la = 2
                if user_sac.city_u != "":
                    content_21[0][2][0][la] = "{}, {:%d de %B de %Y}".format(user_sac.city_u, created_date)
                else:
                    content_21[0][2][0][la] = "Armenia, {:%d de %B de %Y}".format(created_date)
                content_21[0][2][1][la] = "{:%I:%M %p}".format(created_date)
                content_21[1][0] = "REGISTRO DE ASISTENCIA Y APROBACIÓN DEL ACTA No- {} DEL DÍA {:%d DEL MES DE %B DEL AÑO %Y}".format(
                    id_a, created_date).upper()
                content_21[1][3] = [
                    "1",
                    "",
                    user_sac.name_u + " " + user_sac.lastname_u,
                    user_sac.document_u,
                    "",
                    "",
                    "",
                    "Centro de Comercio y Turismo",
                    user_sac.email_inst,
                    user_sac.phone_u,
                    "",
                    ""]
                if user_sac.bonding_type == 1:
                    content_21[1][3][4] = "X"
                elif user_sac.bonding_type == 2:
                    content_21[1][3][5] = "X"
                return content_21
        except Exception:
            return None
        
        
    # content : string - html data
    def get_content_data(self, content):
        body_h = self.extract_body_html(content)
        text_data = self.html_to_text(content)
        header = self.extract_header_data(text_data)
        body_index = header['len_header']
        body_t = self.extract_body_data_v1(
            text_data[body_index:len(text_data)])
        footer_index = body_index + body_t[len(body_t)-1]
        footer = self.extract_footer_data(
            text_data[footer_index:len(text_data)])
        self.document_content = {
            'header': header,
            'body_h': body_h,
            'body_t': body_t,
            'footer': footer
        }
        return self.document_content

    # content : list - html text
    # header_keys : list - dict keys
    def extract_header_data(self, content, header_keys=header_keys):
        header_content = {}
        k = 0
        cont = 0
        for i in range(len(content)):
            if cont == len(headers_colm):
                # header length in content
                header_content['len_header'] = k
                return header_content
            # Unicode to ASCII
            header_col = unidecode(content[k].lower())
            # check first index
            if headers_colm[0] in header_col:
                cont += 1
                header_content[header_keys[0]] = content[0]
                k += 1
            # check last index
            elif headers_colm[len(headers_colm)-1] in header_col:
                cont += 1
                header_content[header_keys[len(header_keys)-1]] = content[k]
                k += 1
            else:
                if headers_colm[i] in header_col:
                    cont += 1
                    header_content[header_keys[i]] = content[k+1]
                    k += 2

    def extract_body_html(self, content):
        body_div = content.split('list-intr')
        body_div[1] = '<ol class="list-intr' + body_div[1]
        body = body_div[1].split('end-deact')
        len_h = len(body[0])-25
        body_h = body[0][:len_h]
        return body_h

    # content : list - html text
    def extract_body_data_v1(self, content):
        body_content = []
        cont = 0
        for i in range(len(content)):
            body_col = unidecode(content[i].lower())
            if body_colm[len(body_colm)-1] in body_col:
                cont += 2
                body_content.append(content[i])
                body_content.append(cont)
                return body_content
            body_content.append(content[i])
            cont += 1

    # content : list - html text
    # body_keys : list - dict keys
    def extract_body_data_v2(self, content, body_keys=body_keys):
        body_content = {}
        cont = 0
        for i in range(len(content)):
            body_col = unidecode(content[i].lower())
            # check keys before and after the value
            if body_colm[i] in body_col and content[i+1] != body_colm[i+1]:
                # check first index
                if body_colm[0] in body_col[i]:
                    cont += 1
                    body_content[body_keys[0]] = content[i+1]
                # check last index
                elif body_colm[5] in body_col[i]:
                    cont += 1
                    body_content[body_keys[2]] = content[i+1]
                    return body_content
                else:
                    # Instructor data
                    pass

    # content : list - html text
    # footer_keys : list - dict keys
    def extract_footer_data(self, content, footer_keys=footer_keys):
        footer_content = {}
        user = {}
        list_user = []
        footer_col = ''
        cont = 6
        for i in range(len(content)):
            footer_col = unidecode(content[i].lower())
            # data before attendance
            if footer_colm[1] in footer_col:
                footer_content[footer_keys[i]] = content[i+3]
            elif footer_colm[2] in footer_col:
                footer_content[footer_keys[i]] = content[i+3]
            elif footer_colm[3] in footer_col:
                footer_content[footer_keys[i]] = content[i+3]
            elif footer_colm[5] in footer_col:
                footer_content[footer_keys[3]] = content[i]
                footer_content[footer_keys[4]] = content[i+1]
                footer_content[footer_keys[5]] = content[i+3]
            elif footer_colm[len(footer_colm)-1] in footer_col:
                # attendance
                for m in range(i+1, len(content)):
                    user[footer_keys[cont]] = content[m]
                    cont += 1
                    if cont == 13:
                        list_user.append(user)
                        user = {}
                        cont = 6
                footer_content['list_asis'] = list_user
                return footer_content


#dt = DocumentTool()
#docHtml = dt.html_to_string('2021.html')
#doc = dt.html_to_string('./2020.html')
#t = open('2021.txt', 'w')
# t.write(docHtml)
# t.close()
