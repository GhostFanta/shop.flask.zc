from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from shop.api.plugins import cors, migrate, marshmallow
from shop.api.settings import ProdConfig, DevConfig
from shop.api.cart.routes import carts_blueprint
from shop.api.shipment.routes import shipment_blueprint
from shop.api.products.routes import products_blueprint
from shop.api.user.routes import user_blueprint
from shop.api.commands import seed, routes


def register_plugins(app):
    from shop.api.plugins import db
    from shop.api.plugins import cli
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
    app.cli.add_command(routes)


def create_app(config_object=ProdConfig):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config_object.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config_object.SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['SWAGGER'] = config_object.SWAGGER
    register_plugins(app)
    register_blueprints(app)
    register_commands(app)
    return app
