from shop.api.plugins import BaseModel, db, relationship, CRUDMixin
from shop.api.enums import OrderStatus

from shop.api.user.models import User
from shop.api.products.models import Product


class Cart(db.Model, CRUDMixin):
    """
    Contains a list of items, which indicates the items that the customer want to
    proceed.
    """
    __tablename__ = 'cart'
    id = db.Column('id', db.Integer, autoincrement=True, nullable=False, unique=True, primary_key=True)
    user_id = db.Column('user_id', db.ForeignKey('user.id'))

    items = db.relationship('Item', backref=db.backref("cart_items"))
    user = db.relationship("User", backref=db.backref("user_cart"))

    def __init__(self, **kwargs):
        db.Model.__init__(self,
                          user_id=kwargs.get('user_id')
                          )


class Item(db.Model, BaseModel, CRUDMixin):
    """
    One row in cart, which contains the info of a product and the number of
    products that the customer want to purchase.
    """
    __tablename__ = 'item'
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=True)
    amount = db.Column('amount', db.Integer, default=0)

    cart = relationship("Cart", backref="item_cart")
    product = relationship("Product", backref="item_product")

    def __init__(self, **kwargs):
        db.Model.__init__(self,
                          product_id=kwargs.get('product_id'),
                          amount=kwargs.get('amount'),
                          cart_id=kwargs.get('cart_id')
                          )

    @property
    def price(self):
        return self.product.price * self.amount


class Order(db.Model, BaseModel, CRUDMixin):
    """
    It represents the proceed cart.
    """

    __tablename__ = 'order'
    status = db.Column('status', db.Enum(OrderStatus), default=OrderStatus.unshipped)
    processed_at = db.Column('processed_at', db.DateTime)

    def __init__(self, **kwargs):
        db.Model.__init__(self,
                          status=kwargs.get('status')
                          )
