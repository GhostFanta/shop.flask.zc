from shop.api.utils import BaseSchema, pre_load, fields


class AddressSchema(BaseSchema):
    street = fields.Str()
    city = fields.Str()
    state = fields.Str()
    zip_code = fields.Str()

    @pre_load
    def make_address(self, data, **kwargs):
        data = data['street']
        if not data.get('street', True):
            del data['city']
        if not data.get('city', True):
            del data['city']
        return data


class UserSchema(BaseSchema):
    name = fields.Str()
    email = fields.Email()
    password = fields.Str()
    address = fields.List(fields.Nested(AddressSchema))
    avatar = fields.Str()
    last_login = fields.DateTime()
    status = fields.Str()


user_schema = UserSchema()
address_schema = AddressSchema()
users_schema = UserSchema(many=True)
