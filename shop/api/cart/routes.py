from flask import Blueprint, jsonify, request
from sqlalchemy import or_, and_
from webargs import fields, ValidationError, flaskparser
from shop.api.user.models import User
from shop.api.products.models import Product
from shop.api.cart.models import Cart, Item, Order
from shop.api.cart.schemas import cart_schema, items_schema, item_in_cart_schema
from shop.api.enums import OrderStatus
from shop.api.exceptions import UserExceptions

from http import HTTPStatus

carts_blueprint = Blueprint('carts', __name__)
parser = flaskparser.FlaskParser()

parser.DEFAULT_VALIDATION_STATUS = 400
use_args = parser.use_args


@carts_blueprint.route('/ping', methods=['GET'])
def pong():
    return jsonify({'pong': True}), HTTPStatus.OK


@carts_blueprint.route('/carts/<user_id>', methods=['GET'])
def get_cart(user_id):
    """
    List all items currently not proceed in cart.
    :param user_id:
    :return:
    """
    cart = Cart.query.filter_by(user_id=user_id).first()
    if not cart:
        cart = Cart(user_id=user_id)
        cart.save()
    return cart_schema.dump(cart), HTTPStatus.OK


@carts_blueprint.route('/carts/<user_id>', methods=['DELETE'])
def clear_cart(user_id):
    """
    Physically delete item from a cart, bulk delete supported.
    :param user_id:
    :return:
    """
    cart = Cart.query.filter_by(user_id=user_id).first()
    if not cart:
        cart = Cart(user_id=user_id)
        cart.save()
    item = Item.delete_many(Item.cart_id == cart.id)
    return jsonify({"num": item}), HTTPStatus.NO_CONTENT


@carts_blueprint.route('/carts/<user_id>/items', methods=['POST'])
def add_item_to_cart(user_id):
    data = request.json
    cart = Cart.query.filter_by(user_id=user_id).first()
    if not cart:
        cart = Cart(user_id=user_id)
        cart.save()
    item = Item(cart_id=cart.id, **data)
    item.save()
    Product.add_amount(**data)
    return jsonify(cart_schema.dump(cart)), HTTPStatus.OK


@carts_blueprint.route('/carts/<user_id>', methods=['POST'])
def checkout(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return UserExceptions.user_not_exist, HTTPStatus.BAD_REQUEST
    cart = Cart.query.filter_by(user_id=user_id).first()
    if not cart:
        cart = Cart(user_id=user_id)
        cart.save()
    items = Item.query.filter_by(cart_id=cart.id, order_id=None).all()
    if not items:
        return jsonify({}), HTTPStatus.NOT_FOUND
    order = Order(status=OrderStatus.pending)
    order.save()
    for item in items:
        item.update(order_id=order.id)
        item.save()
    return jsonify({}), HTTPStatus.OK


@carts_blueprint.route('/items/<item_id>', methods=['DELETE'])
def delete_item_from_cart(item_id):
    Item.get(item_id).delete()
    return jsonify({}), HTTPStatus.NO_CONTENT


@carts_blueprint.route('/items/<item_id>', methods=['PUT', 'PATCH'])
def update_item_in_cart(item_id):
    data = request.json
    item = Item.get(item_id).update(**data)
    return jsonify(item_in_cart_schema.dump(item)), HTTPStatus.OK
