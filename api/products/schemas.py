from marshmallow import Schema, fields, post_dump


class TagSchema(Schema):
    tagname = fields.Str()


class CategorySchema(Schema):
    categoryname = fields.Str()


class ProductSchema(Schema):
    name = fields.Str()
    price = fields.Decimal()
    rating = fields.Int()
    capacity = fields.Int()
    category = fields.Nested(CategorySchema)
    produced_at = fields.DateTime()
