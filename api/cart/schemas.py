from marshmallow import Schema, fields, pre_load, post_dump


class ItemSchema(Schema):
    productname = fields.Str()
    amount = fields.Number()
    price = fields.Number()


class CartSchema(Schema):
    username = fields.Str()
    item = fields.List(fields.Nested(ItemSchema))


class OrderSchema(Schema):
    pass


cart_schema = CartSchema()
item_schema = ItemSchema()
order_schema = OrderSchema()
