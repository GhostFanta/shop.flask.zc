from flask_sqlalchemy import SQLAlchemy, Model
from sqlalchemy.orm import relationship
from flask_migrate import Migrate
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime


class CRUDMixin(Model):
    @classmethod
    def create(cls, **kwargs):
        row = cls(**kwargs)
        return row.save()

    def update(self, commit=True, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)
        return commit and self.save() or self

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        return commit and db.session.commit()


db = SQLAlchemy(model_class=CRUDMixin)
migrate = Migrate()
cors = CORS()
marshmallow = Marshmallow()

Column = db.Column
relationship = relationship
Model = db.Model


class SoftDeleteMixin(CRUDMixin):
    def delete(self, commit=True):
        deleted_at = db.Column('deleted_at', db.DateTime, nullable=True)


class BaseModel(object):
    id = db.Column('id', db.Integer, autoincrement=True, nullable=False, unique=True, primary_key=True)
    created_at = db.Column('created_at', db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column('updated_at', db.DateTime, nullable=False, default=datetime.utcnow())
