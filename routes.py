from controllers.signin import Signin
signin = {
    "signin": "/signin", "view_func_signin": Signin.as_view("app_signin")
}