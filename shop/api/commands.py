from flask_cli import with_appcontext
from flask import current_app
from datetime import datetime

from shop.api.user.models import User, Address
from shop.api.shipment.models import Shipment
from shop.api.products.models import Product, ProductReview, Category

from shop.api.enums import AccountStatus

import click
import operator


@click.command()
@with_appcontext
def seed():
    print("Seeding...")
    User.create(commit=True, name='user1', email='test1@alex.me', password='123456',
                avatar='http://dummyimage.com/250x250.jpg/dddddd/000000',
                last_login=datetime.utcnow(), status=AccountStatus.active)
    User.create(commit=True, name='user2', email='test2@alex.me', password='123456',
                avatar='http://dummyimage.com/250x250.jpg/dddddd/000000',
                last_login=datetime.utcnow(), status=AccountStatus.active)
    Address.create(street='stree1', city='city1', state='state1', zip_code='0000000', user_id=1)
    Address.create(street='stree2', city='city2', state='state2', zip_code='0000002', user_id=2)
    Category.create(category_name='cat1')
    Category.create(category_name='cat2')
    Product.create(product_name='product1', description='product_des1', price='11', produced_at=datetime.utcnow(),
                   capacity=11, category_id=1)
    Product.create(product_name='product2', description='product_des2', price='22', produced_at=datetime.utcnow(),
                   capacity=22, category_id=2)
    ProductReview.create(rating=3, review="Good product1!", product_id=1)
    ProductReview.create(rating=3, review="Good product2!", product_id=2)


@click.command()
@with_appcontext
def routes():
    """Display registered routes"""
    rules = []
    for rule in current_app.url_map.iter_rules():
        methods = ','.join(sorted(rule.methods))
        rules.append((rule.endpoint, methods, str(rule)))

    sort_by_rule = operator.itemgetter(2)
    for endpoint, methods, rule in sorted(rules, key=sort_by_rule):
        route = '{:50s} {:25s} {}'.format(endpoint, methods, rule)
        print(route)
