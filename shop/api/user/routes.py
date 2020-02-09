from flask import Blueprint, jsonify, request
from webargs import fields, ValidationError, flaskparser
from webargs.flaskparser import use_args
from shop.api.user.models import User, Address
from shop.api.exceptions import UserExceptions
from datetime import datetime

from shop.api.user.schemas import users_schema, user_schema

from http import HTTPStatus

user_blueprint = Blueprint('user', __name__)
parser = flaskparser.FlaskParser()

parser.DEFAULT_VALIDATION_STATUS = 400
use_args = parser.use_args


@user_blueprint.route('/users/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.get_or_404(user_id)
    if not user:
        return UserExceptions.user_not_exist(), HTTPStatus.NOT_FOUND
    return user_schema.dump(user), HTTPStatus.OK


@user_blueprint.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    if not users:
        return UserExceptions.user_not_exist(), HTTPStatus.NOT_FOUND
    return jsonify(users_schema.dump(users)), HTTPStatus.OK


@user_blueprint.route('/users/<user_id>', methods=['PUT', 'PATCH'])
def update_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    data = request.json
    if not user:
        return UserExceptions.user_not_exist(), HTTPStatus.NOT_FOUND
    user.update(updated_at=datetime.utcnow(), **data)
    return jsonify(user_schema.dump(user)), HTTPStatus.OK


@user_blueprint.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = User.create(**data)
    if hasattr(data, 'address'):
        address = Address.create(**data['address'][0], user_id=user.id)
        user.address = [address]
    return jsonify(user_schema.dump(user)), HTTPStatus.OK


@user_blueprint.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return '', HTTPStatus.NOT_FOUND
    user.delete()
    return '', HTTPStatus.NO_CONTENT
