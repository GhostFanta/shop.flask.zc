class BaseConfig(object):
    pass


class ProdConfig(BaseConfig):
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3365/shop'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@mysql:3306/shop'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3365/shop'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
