from controllers.login import Login
from controllers.signin import Signin, SigninExtra
from controllers.document import Document


login = {
    "login": "/login", "view_func_login": Login.as_view("app_login")
}

signin = {
    "signin": "/signin", "view_func_signin": Signin.as_view("app_signin"),
    "signinExtra": "/editprofile", "view_func_signinExtra": SigninExtra.as_view("app_signinExtra")
}

document = {
    "document": "/document", "view_func_document": Document.as_view("app_document")
}
