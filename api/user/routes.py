from flask import Blueprint, jsonify, request
from webargs import fields, ValidationError, flaskparser
from webargs.flaskparser import use_args
from api.user.models import User
from api.exceptions import UserExceptions

from api.user.schemas import users_schema, user_schema

from http import HTTPStatus

user_blueprint = Blueprint('user', __name__)
parser = flaskparser.FlaskParser()

parser.DEFAULT_VALIDATION_STATUS = 400
use_args = parser.use_args


@user_blueprint.route('/users/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        raise UserExceptions.user_not_exist()
    return user_schema.dump(user), HTTPStatus.OK


@user_blueprint.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    if not users:
        raise UserExceptions.user_not_exist()
    return jsonify(users_schema.dump(users)), HTTPStatus.OK


@user_blueprint.route('/users/<user_id>', methods=['PUT', 'PATCH'])
def update_user(user_id):
    user = User.query.filter_by(id=user_id)
    data = request.json
    if not user:
        raise UserExceptions.user_not_exist()
    user.update(data)
    return jsonify(users_schema.dump(user))


@user_blueprint.route('/users', methods=['POST'])
def create_user():
    pass


@user_blueprint.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id)
    user.delete()
    return user
