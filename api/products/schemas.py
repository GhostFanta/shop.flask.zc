from marshmallow import Schema, fields, post_dump


class TagSchema(Schema):
    tag_name = fields.Str()


class CategorySchema(Schema):
    category_name = fields.Str()


class ProductReviewSchema(Schema):
    rating = fields.Number()
    review = fields.String()


class ProductSchema(Schema):
    id = fields.Integer()
    name = fields.Str()
    price = fields.Decimal()
    capacity = fields.Int()
    category = fields.Nested(CategorySchema)
    produced_at = fields.DateTime()
    reviews = fields.List(fields.Nested(ProductReviewSchema))


tag_schema = TagSchema()
category_schema = CategorySchema()
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
