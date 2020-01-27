from api.plugins import CRUDMixin, BaseModel, db, relationship


class Category(db.Model, BaseModel, CRUDMixin):
    __tablename__ = 'category'
    category_name = db.Column('category_name', db.String(20))

    # product = db.relationship("Product", backref="category")

    def __init__(self, **kwargs):
        self.__category_name = kwargs.get('category_name')

    def __repr__(self):
        return '<Category %r>' % self.__category_name


class Product(db.Model, BaseModel, CRUDMixin):
    __tablename__ = 'product'
    product_name = db.Column('product_name', db.String(200))
    description = db.Column('description', db.String(200))
    price = db.Column('price', db.DECIMAL)
    capacity = db.Column('capacity', db.String(200))
    # category_id = db.Column('category', db.ForeignKey('category.id'))
    category_id = db.Column('category', db.Integer)

    # item = relationship('Item', backref="product")
    # category = relationship('Category', backref="product")

    def __init__(self, **kwargs):
        self.__product_name = kwargs.get('product_name')
        self.__description = kwargs.get('description')
        self.__price = kwargs.get('price')
        self.__capacity = kwargs.get('capacity')
        self.__category = kwargs.get('category')


class ProductReview(db.Model, BaseModel, CRUDMixin):
    __tablename__ = 'productreview'
    rating = db.Column('rating', db.Integer)
    review = db.Column('review', db.Text)

    def __init__(self, **kwargs):
        self.__rating = kwargs.get('rating')
        self.__review = kwargs.get('review')


class Tag(db.Model, BaseModel, CRUDMixin):
    __tablename__ = 'tag'
    tag_name = db.Column('tag_name', db.String(20))

    def __init__(self, **kwargs):
        self.__name = kwargs.get('tag_name')
