from flask import Blueprint, jsonify, request
from webargs import fields, ValidationError, flaskparser
from webargs.flaskparser import use_args
from api.products.models import ProductReview, Product
from api.exceptions import ProductException
from api.products.schemas import product_schema, products_schema

from http import HTTPStatus

products_blueprint = Blueprint('products', __name__)
parser = flaskparser.FlaskParser()

parser.DEFAULT_VALIDATION_STATUS = 400
use_args = parser.use_args


@products_blueprint.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    if not products:
        raise ProductException.no_products_in_db()
    return jsonify(products_schema.dump(products)), HTTPStatus.OK


@products_blueprint.route('/products/<product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = Product.query.filter(id=product_id)
    if not product:
        raise ProductException.product_not_exist()
    return product_schema.dump(product), HTTPStatus.OK


@products_blueprint.route('/products', methods=['POST'])
def create_product():
    data = request.json
    product = Product.create(**data)
    return product_schema.dump(product), HTTPStatus.OK


@products_blueprint.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.filter_by(id=product_id).first()
    if not product:
        raise ProductException.product_not_exist()
    product.delete()
    return products_schema.dump(product), HTTPStatus.NO_CONTENT


@products_blueprint.route('/products/<product_id>/product_reviews', methods=['GET'])
def get_product_view_by_product_id(product_id):
    reviews = ProductReview.query.filter(product_id=product_id)
    if not reviews:
        raise ProductException.no_product_review()
    return reviews


@products_blueprint.route('/products/<product_id>/product_reviews/<review_id>', methods=['GET'])
def get_product_view_by_product_id_and_review_id(product_id, review_id):
    reviews = ProductReview.query.filter(product_id=product_id, id=review_id)
    if not reviews:
        raise ProductException.no_product_review()
    return reviews
