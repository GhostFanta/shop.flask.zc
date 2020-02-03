from flask import current_app
from flask_cli import with_appcontext
from datetime import datetime

from api.user.models import User
from api.enums import AccountStatus

import click


@click.command()
@with_appcontext
def seed():
    print("seed command")
    user1 = User(name='user1', email='test1@alex.me', password='123456',
                 avatar='http://dummyimage.com/250x250.jpg/dddddd/000000',
                 last_login=datetime.now(), status=AccountStatus.active).save()
    user1 = User(name='user2', email='test2@alex.me', password='123456',
                 avatar='http://dummyimage.com/250x250.jpg/dddddd/000000',
                 last_login=datetime.now(), status=AccountStatus.active).save()
