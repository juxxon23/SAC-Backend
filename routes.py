from controllers.login import Login
from controllers.signin import Signin, SigninExtra
from controllers.document import Document

user = {
    "signin": "/signin", "view_func_signin": Signin.as_view("app_signin"),
    "login": "/login", "view_func_login": Login.as_view("app_login")
}

<<<<<<< HEAD
signin = {
    "signin": "/signin", "view_func_signin": Signin.as_view("app_signin"),
    "signinExtra": "/editprofile", "view_func_signinExtra": SigninExtra.as_view("app_signinExtra")
}

=======
>>>>>>> b35f639dfb78ca56d4708a6c740779dc8e619eb8
document = {
    "document": "/document", "view_func_document": Document.as_view("app_document")
}
