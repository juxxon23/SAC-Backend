from db.postgresql.model import db
from sqlalchemy.exc import SQLAlchemyError


class PostgresqlManager():
    def add(self, *args):
        for new in args:
                db.session.add(new)
                db.session.commit()
        return 'ok'

    def update(self):
        try:
            db.session.commit()
            return 'ok'
        except SQLAlchemyError as e:
            return e
        except:
            return 'error'

    def delete(self, obj):
        try:
            db.session.delete(obj)
            db.session.commit()
            return 'ok'
        except SQLAlchemyError as e:
            return e
        except:
            return 'error'

    def get_all(self, table_name):
        try:
            data = db.session.query(table_name).all()
            return data
        except SQLAlchemyError as e:
            return e
        except:
            return 'error'

    # table.query.filter_by(col=data).first()
    def get_by(self, table_name, value):
        try:
            data = db.session.query(table_name).filter_by(document_u = value).first()
            return data
        except SQLAlchemyError as e:
            return e
        except:
            return 'error in consulta'