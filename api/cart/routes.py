from flask import Blueprint, jsonify
from webargs import fields, ValidationError, flaskparser
from webargs.flaskparser import use_args

from http import HTTPStatus

carts = Blueprint('carts', __name__)
parser = flaskparser.FlaskParser()

parser.DEFAULT_VALIDATION_STATUS = 400
use_args = parser.use_args


@carts.route('/ping', methods=['GET'])
def pong():
    return jsonify({'pong': True}), HTTPStatus.OK


@carts.route('/carts/:id', methods=['GET'])
def getProducts():
    pass
