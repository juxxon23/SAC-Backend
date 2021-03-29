from flask import Flask
from app.db.postgresql.model import db, Bonding, User, InfoStats
from app.db.postgresql.postgresql_manager import PostgresqlManager
from app.helpers.error_handler import PostgresqlError


def create_app():
    pse = PostgresqlError()
    postgreql_tool = PostgresqlManager()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pass123@localhost:5432/sac-ddb'
    with app.app_context():
        db.init_app(app)
        db.create_all()
        num_act = postgreql_tool.get_num_act(InfoStats, "curr_act")
        msg = pse.msg(num_act)
        if msg.get('status') != 'ok':
            max_act = InfoStats(
                code_value='curr_act',
                value_info=000,
                description="Numero actual de acta"
            )
            postgreql_tool.add(max_act)
        bonding_list = postgreql_tool.get_all(Bonding)
        msg = pse.msg(num_act)
        if msg.get('status') == 'ok':
            if len(bonding_list) == 3:
                return app
            else:
                contratista = Bonding(description='Contratista')
                planta = Bonding(description='Planta')
                default = Bonding(description='Defecto')
                postgreql_tool.add(contratista, planta, default)
                return app
