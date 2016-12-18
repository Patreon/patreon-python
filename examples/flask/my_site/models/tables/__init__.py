from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from my_site.models.tables.my_model import MyModel


class MySQLAlchemy(SQLAlchemy):
    def make_declarative_base(self):
        from flask.ext.sqlalchemy import _BoundDeclarativeMeta, _QueryProperty
        base = declarative_base(cls=MyModel, name='MyModel', metaclass=_BoundDeclarativeMeta)
        base.query = _QueryProperty(self)
        return base

db = MySQLAlchemy()
