from controllers.signin import Signin
from controllers.document import Document


signin = {
    "signin": "/signin", "view_func_signin": Signin.as_view("app_signin")
}

document = {
    "document": "/document", "view_func_document": Document.as_view("app_document")
}