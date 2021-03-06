from .controllers.login import Login
from .controllers.signin import Signin
from .controllers.document import Document
from .controllers.check import Check
from .controllers.search import Search
from .controllers.req_edit import ReqEdit
from .controllers.upfiles import Upfiles

user = {
    "signin": "/signin", "view_func_signin": Signin.as_view("app_signin"),
    "login": "/login", "view_func_login": Login.as_view("app_login")
}

document = {
    "document": "/document", "view_func_document": Document.as_view("app_document"),
    "search": "/search", "view_func_search": Search.as_view("app_search")
}

utils = {
    "ch": "/ch", "view_func_ch": Check.as_view("app_check"),
    "re": "/re", "view_func_re": ReqEdit.as_view("app_reqedit"),
    "up": "/up", "view_func_up": Upfiles.as_view("app_uploads")
}
