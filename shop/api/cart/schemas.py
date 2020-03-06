from marshmallow import Schema, fields, pre_load, post_dump
from shop.api.products.schemas import ProductSchema


class ItemSchema(Schema):
    item_id = fields.Integer(attribute='id')
    product = fields.Nested(ProductSchema)
    amount = fields.Number()
    price = fields.Number()


class ItemInCartSchema(Schema):
    item_id = fields.Integer(attribute='id')
    product = fields.Nested(ProductSchema(exclude=['reviews']))
    amount = fields.Number()
    price = fields.Number()


class CartSchema(Schema):
    id = fields.Integer()
    user_id = fields.Integer()
    items = fields.List(fields.Nested(ItemSchema))

    @pre_load
    def filter_not_processed_item(self, in_data, **kwargs):
        in_data['items'] = [item for item in in_data['items'] if item['order_id'] is None]
        return in_data


class OrderSchema(Schema):
    pass


cart_schema = CartSchema()
item_schema = ItemSchema()
item_in_cart_schema = ItemInCartSchema()
items_in_cart_schema = ItemInCartSchema(many=True)
items_schema = ItemSchema(many=True)
order_schema = OrderSchema()
