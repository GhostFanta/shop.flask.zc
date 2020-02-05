from factory.alchemy import SQLAlchemyModelFactory
from api.plugins import db


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = db.session
