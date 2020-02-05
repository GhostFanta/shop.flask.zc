from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from api.plugins import cors, migrate, marshmallow
from api.settings import ProdConfig, DevConfig
from api.cart.routes import carts_blueprint
from api.shipment.routes import shipment_blueprint
from api.products.routes import products_blueprint
from api.user.routes import user_blueprint
from api.commands import seed


def register_plugins(app):
    from api.cart.models import Item, Cart, Order
    from api.shipment.models import Shipment, ShipmentTrack
    from api.products.models import Product, ProductReview, Category, Tag
    from api.user.models import User, Address
    from api.plugins import db
    from api.plugins import cli
    cli.init_app(app)
    db.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)
    marshmallow.init_app(app)


def init_swagger(app):
    SWAGGER_URL = '/docs'
    API_URL = '/static/swagger.json'
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(SWAGGER_URL,
                                                  API_URL, config={
            'app_name': 'Shop the API'
        })
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


def register_blueprints(app):
    app.register_blueprint(carts_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(products_blueprint)
    app.register_blueprint(shipment_blueprint)
    init_swagger(app)


def register_commands(app):
    app.cli.add_command(seed)


def create_app(config_object=ProdConfig):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config_object.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config_object.SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['SWAGGER'] = config_object.SWAGGER
    register_plugins(app)
    register_blueprints(app)
    register_commands(app)
    return app
