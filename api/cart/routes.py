from flask import Blueprint, jsonify
from webargs import fields, ValidationError, flaskparser
from webargs.flaskparser import use_args
from api.cart.models import Cart
from api.cart.schemas import cart_schema

from http import HTTPStatus
from api.exceptions import ProductException

carts_blueprint = Blueprint('carts', __name__)
parser = flaskparser.FlaskParser()

parser.DEFAULT_VALIDATION_STATUS = 400
use_args = parser.use_args


@carts_blueprint.route('/ping', methods=['GET'])
def pong():
    return jsonify({'pong': True}), HTTPStatus.OK


@carts_blueprint.route('/carts/<user_id>', methods=['GET'])
def get_cart(user_id):
    cart = Cart.query.filter_by(user_id=user_id)
    if not cart:
        raise ProductException.product_not_exist()
    return cart_schema.dump(cart), HTTPStatus.OK
