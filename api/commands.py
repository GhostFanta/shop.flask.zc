from flask import current_app
from flask_cli import with_appcontext
from datetime import datetime

from api.user.models import User
from api.shipment.models import Shipment
from api.products.models import Product, ProductReview

from api.enums import AccountStatus

import click


@click.command()
@with_appcontext
def seed():
    print("Seeding...")
    User.create(commit=True, name='user1', email='test1@alex.me', password='123456',
                avatar='http://dummyimage.com/250x250.jpg/dddddd/000000',
                last_login=datetime.now(), status=AccountStatus.active)
    User.create(commit=True, name='user2', email='test2@alex.me', password='123456',
                avatar='http://dummyimage.com/250x250.jpg/dddddd/000000',
                last_login=datetime.now(), status=AccountStatus.active)
