from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Signin(db.Model):
    __tablename__ = 'Signin'

    id_signin = db.Column(db.Integer, primary_key=True, index=True)
    document_u = db.Column(db.String(20), nullable=False)
    email_inst = db.Column(db.String(50), nullable=False)
    password_u = db.Column(db.String(128), nullable=False)
    name_u = db.Column(db.String(30), nullable=False)
    lastname_u = db.Column(db.String(30), nullable=False)
    phone_u = db.Column(db.String(10), nullable=False)
    regional_u = db.Column(db.String(100), nullable=False)
    centro_u = db.Column(db.String(100), nullable=False)
    competencies_u = db.Column(db.String(50), nullable=False)
    results_u = db.Column(db.String(50),nullable=False)
    bonding_type = db.Column(db.String(11), nullable=False)

    def __init__(self, id_signin, document_u, email_inst, password_u, name_u, lastname_u, phone_u, regional_u, centro_u, competencies_u, results_u,bonding_type):
        self.id_signin = id_signin
        self.document_u = document_u
        self.email_inst = email_inst
        self.password_u = password_u
        self.name_u = name_u
        self.lastname_u = lastname_u
        self.phone_u = phone_u
        self.regional_u = regional_u
        self.centro_u = centro_u
        self.competencies_u = competencies_u
        self.results_u = results_u
        self.bonding_type = bonding_type