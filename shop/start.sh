#!/bin/sh
export FLASK_APP=/shop/app.py
flask db init
flask db migrate
flask db upgrade
flask seed
gunicorn --workers 2 --bind 0.0.0.0:5000 "shop.api:create_app()"