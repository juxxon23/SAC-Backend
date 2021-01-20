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
    def read_html(self, path):
        with open(path, "r") as file_html:
            string_data = file_html.read()
            return string_data
