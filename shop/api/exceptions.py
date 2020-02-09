from flask import jsonify


def template(data, code):
    return {'message': {'errors': {'body': data}}, 'status_code': code}


USER_NOT_FOUND = template(['User not exist'], code=404)
PRODUCT_DB_EMPTY = template(['No products exist in db'], code=404)
PRODUCT_NOT_FOUND = template(['Product not exist'], code=404)
NO_PRODUCT_REVIEW = template(['Product review is empty'], code=404)


class ProductException(object):
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        object.__init__(self)
        self.message = message

        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def __repr__(self):
        return {'message': self.message, 'status_code': self.status_code}

    @classmethod
    def product_not_exist(cls):
        return jsonify(cls(**PRODUCT_NOT_FOUND).__str__())

    @classmethod
    def no_products_in_db(cls):
        return cls(**PRODUCT_DB_EMPTY).__str__()

    @classmethod
    def no_product_review(cls):
        return cls(**NO_PRODUCT_REVIEW).__str__()


class UserExceptions(object):
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message

        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    @classmethod
    def user_not_exist(cls):
        return cls(**USER_NOT_FOUND).__str__()
