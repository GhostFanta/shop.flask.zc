from flask_sqlalchemy import SQLAlchemy, Model
from flask import abort
from sqlalchemy.orm import relationship
from flask_migrate import Migrate
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_cli import FlaskCLI

from datetime import datetime


class CRUDMixin(Model):
    @classmethod
    def query(cls):
        return db.session.query(cls)

    @classmethod
    def get(cls, _id):
        if any((isinstance(_id, str) and _id.isdigit(),
                isinstance(_id, (int, float))), ):
            return cls.query.get(int(_id))
        return None

    @classmethod
    def get_by(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def get_or_404(cls, _id):
        rv = cls.get(_id)
        if rv is None:
            abort(404)
        return rv

    @classmethod
    def get_or_create(cls, **kwargs):
        r = cls.get_by(**kwargs)
        if not r:
            r = cls(**kwargs)
            db.session.add(r)
        return r

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            try:
                db.session.commit()
            except Exception:
                db.session.rollback()
                raise
        return self

    def delete(self, commit=True):
        """
        Physically delete one row
        :param commit:
        :return:
        """
        db.session.delete(self)
        return commit and db.session.commit()

    @classmethod
    def delete_many(cls, conditions, commit=True):
        """
        Do bulk physical delete based on combination of rules.
        :param conditions:
        :param commit:
        :return:
        """
        cls.query.filter(conditions).delete()
        return commit and db.session.commit()


db = SQLAlchemy(model_class=CRUDMixin)
migrate = Migrate()
cors = CORS()
marshmallow = Marshmallow()
cli = FlaskCLI()

Column = db.Column
relationship = relationship
Model = db.Model


class SoftDeleteMixin(CRUDMixin):
    deleted_at = db.Column('deleted_at', db.DateTime, nullable=True)

    def delete(self, commit=True):
        self.deleted_at = datetime.utcnow()
        return commit and db.session.commit()

    @classmethod
    def delete_many(cls, conditions, commit=True):
        pass


class BaseModel(object):
    """
    Primary key and time stamp
    """
    __tablename__ = 'basemodel'
    id = db.Column('id', db.Integer, autoincrement=True, nullable=False, unique=True, primary_key=True)
    created_at = db.Column('created_at', db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column('updated_at', db.DateTime, nullable=False, default=datetime.utcnow())
