class CustomExceptions(Exception):
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message

        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    @classmethod
    def user_not_exist(cls):
        return 'User Not Exist'
