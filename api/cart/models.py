from api.plugins import CRUDMixin, BaseModel, db
from api.enums import OrderStatus

from api.user.models import User
from api.products.models import Product


class Cart(db.Model, CRUDMixin):
    """
    Contains a list of items, which indicates the items that the customer want to
    proceed.
    """
    __tablename__ = 'cart'
    id = db.Column('id', db.Integer, autoincrement=True, nullable=False, unique=True, primary_key=True)
    # user_id = db.Column('user_id', db.ForeignKey('user.id'))
    user_id = db.Column('user_id', db.Integer)

    # items = db.relationship('Item', backref="cart")
    # user = db.relationship("User", back_populates="user")

    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id')


class Item(db.Model, BaseModel, CRUDMixin):
    """
    One row in cart, which contains the info of a product and the number of
    products that the customer want to purchase.
    """
    __tablename__ = 'item'
    # product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    product_id = db.Column('product_id', db.Integer)
    # cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    cart_id = db.Column('cart_id', db.Integer)
    amount = db.Column('amount', db.Integer, default=0)

    # cart = db.relationship("Cart", backref="item")
    # product = db.relationship("Product", backref="item")

    def __init__(self, product_id, amount):
        self._product_id = product_id
        self._amount = amount

    @property
    def price(self):
        pass

# class Order(BaseModel, CRUDMixin):
#     """
#     It represents the proceed cart.
#     """
#
#     __tablename__ = 'order'
#     status = db.Column('status', db.Enum(OrderStatus), default=OrderStatus.unshipped)
#
#     def __init__(self, **kwargs):
#         self.status = kwargs.get('status')
