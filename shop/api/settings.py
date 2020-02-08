class BaseConfig(object):
    pass


class ProdConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3365/shop'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER = {
        "swagger_version": "2.0",
        "title": "Flasgger",
        "headers": [
            ('Access-Control-Allow-Origin', '*'),
            ('Access-Control-Allow-Methods', "GET, POST, PUT, DELETE, OPTIONS"),
            ('Access-Control-Allow-Credentials', "true"),
        ],
        "specs": [
            {
                "version": "0.0.1",
                "title": "Shop the API",
                "endpoint": 'v1_spec',
                "description": 'This is the version 1 of our API',
                "route": '/',
                # rule_filter is optional
                # it is a callable to filter the views to extract
                "rule_filter": lambda rule: rule.endpoint.startswith(
                    'should_be_v1_only'
                ),
                # definition_filter is optional
                # it is a callable to filter the definition models to include
                "definition_filter": lambda definition: (
                        'v1_model' in definition.tags)
            },
        ]
    }


class DevConfig(BaseConfig):
    pass
