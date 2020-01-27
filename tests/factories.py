import json
from factory import PostGenerationMethodCall, Sequence
from factory.alchemy import SQLAlchemyModelFactory
from api import db


class BaseFactory(SQLAlchemyModelFactory):
    pass
