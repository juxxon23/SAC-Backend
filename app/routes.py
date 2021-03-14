from .controllers.login import Login
from .controllers.signin import Signin
from .controllers.document import Document
from .controllers.check import Check

user = {
    "signin": "/signin", "view_func_signin": Signin.as_view("app_signin"),
    "login": "/login", "view_func_login": Login.as_view("app_login")
}

document = {
    "document": "/document", "view_func_document": Document.as_view("app_document")
}

utils = {
    "ch": "/ch", "view_func_ch": Check.as_view("app_check")
}
