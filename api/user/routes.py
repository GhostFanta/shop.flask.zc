from flask import Blueprint, jsonify, request
from webargs import fields, ValidationError, flaskparser
from flasgger import swag_from
from webargs.flaskparser import use_args
from api.user.models import User, Address
from api.exceptions import UserExceptions
from datetime import datetime

from api.user.schemas import users_schema, user_schema

from http import HTTPStatus

user_blueprint = Blueprint('user', __name__)
parser = flaskparser.FlaskParser()

parser.DEFAULT_VALIDATION_STATUS = 400
use_args = parser.use_args


@user_blueprint.route('/users/<user_id>', methods=['GET'])
@swag_from('./docs/get_user_by_id.yml')
def get_user_by_id(user_id):
    """
    tags:
        - User
    parameters:
        - name: user_id
        in: path
        type: integer
        required: true,
        description: user id
    responses:
        200:
            description: Return a list of users
            schema:
            $ref: '#/definitions/
    """
    user = User.get_or_404(user_id)
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
    user = User.query.filter_by(id=user_id).first()
    data = request.json
    if not user:
        raise UserExceptions.user_not_exist()
    user.update(updated_at=datetime.utcnow(), **data)
    return jsonify(user_schema.dump(user)), HTTPStatus.OK


@user_blueprint.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = User.create(**data)
    return jsonify(user_schema.dump(user)), HTTPStatus.OK


@user_blueprint.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return '', HTTPStatus.NOT_FOUND
    user.delete()
    return '', HTTPStatus.NO_CONTENT
