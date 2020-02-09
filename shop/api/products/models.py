from shop.api.plugins import BaseModel, db, relationship, CRUDMixin


class Category(db.Model, CRUDMixin, BaseModel):
    __tablename__ = 'category'
    category_name = db.Column('category_name', db.String(20))

    product = db.relationship("Product", backref="category_product")

    def __init__(self, **kwargs):
        db.Model.__init__(self, category_name=kwargs.get('category_name'))

    def __repr__(self):
        return '<Category %r>' % self.__category_name


class Product(db.Model, CRUDMixin, BaseModel):
    __tablename__ = 'product'
    product_name = db.Column('product_name', db.String(200))
    description = db.Column('description', db.String(200))
    price = db.Column('price', db.DECIMAL)
    produced_at = db.Column('produced_at', db.DateTime)
    capacity = db.Column('capacity', db.String(200))
    category_id = db.Column('category', db.ForeignKey('category.id'))

    item = relationship('Item', backref="item_product")
    category = relationship('Category', backref=db.backref("product_category"))
    reviews = relationship('ProductReview', backref=db.backref("product_review"))

    def __init__(self, **kwargs):
        db.Model.__init__(self,
                          product_name=kwargs.get('product_name'),
                          description=kwargs.get('description'),
                          price=kwargs.get('price'),
                          capacity=kwargs.get('capacity'),
                          category=kwargs.get('category'),
                          )


class ProductReview(db.Model, CRUDMixin, BaseModel):
    __tablename__ = 'productreview'
    rating = db.Column('rating', db.Integer)
    review = db.Column('review', db.Text)
    product_id = db.Column('product_id', db.ForeignKey('product.id'))

    product = relationship('Product', backref=db.backref('productreview'))

    def __init__(self, **kwargs):
        db.Model.__init__(
            self,
            rating=kwargs.get('rating'),
            review=kwargs.get('review'),
            product_id=kwargs.get('product_id')
        )


class Tag(db.Model, BaseModel):
    __tablename__ = 'tag'
    tag_name = db.Column('tag_name', db.String(20))

    def __init__(self, **kwargs):
        db.Model.__init__(self,
                          name=kwargs.get('tag_name')
                          )
