from flask import Flask
from flask_cors import CORS
from routes import signin
from db.postgresql.model import db

app = Flask(__name__)
CORS(app, support_credentials= True)

# Signin routes
app.add_url_rule(signin['signin'], view_func= signin['view_func_signin'])
