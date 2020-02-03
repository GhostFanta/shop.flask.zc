from flask import Blueprint, jsonify
from webargs import fields, ValidationError, flaskparser
from webargs.flaskparser import use_args
from api.cart.models import Cart

from http import HTTPStatus
from api.exceptions import ProductException

carts_blueprint = Blueprint('carts', __name__)
parser = flaskparser.FlaskParser()

parser.DEFAULT_VALIDATION_STATUS = 400
use_args = parser.use_args


@carts_blueprint.route('/ping', methods=['GET'])
def pong():
    return jsonify({'pong': True}), HTTPStatus.OK


@carts_blueprint.route('/carts/:id', methods=['GET'])
def get_cart():
    cart = Cart.query.filter_by()
    if not cart:
        raise ProductException.product_not_exist()
    return cart, HTTPStatus.OK
