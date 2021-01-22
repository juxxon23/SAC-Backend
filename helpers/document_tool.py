from pydocx import PyDocX

class DocumentTool():
    """
    Document Tool
    """

    # path: string - docx path
    # outname: string - filename
    def docx_to_html(self, path, outname):
        with open(outname, "w") as file_html:
            html = PyDocX.to_html(path)
            file_html.write(html)
            return html

    # path: string - html path
    @staticmethod
    def read_html(path):
        with open(path, "r") as file_html:
            string_data = file_html.read()
            return string_data

    
    def format_html_string(self, html_format_path):
        html_string = DocumentTool.read_html(html_format_path)
        split_html = html_string.split('\n')        # Split donde exista un salto de linea
        for i in range(len(split_html)):
            split_html[i] = split_html[i].strip()   # Borra espacios al principio y final de cada string
        split_html.insert(0, "'")                   # Se inserta el caracter en el indice 0
        split_html.insert(len(split_html), "'")     # # Se inserta el caracter en el ultimo indice
        sep = ''
        split_html = sep.join(split_html)           # Se une cada indice del arreglo con sep
        return split_html 


dt = DocumentTool()
result = dt.format_html_string("./ActaCierre.html")
test = open("format_html_string_here.txt", "w")
test.write(result)
test.close()