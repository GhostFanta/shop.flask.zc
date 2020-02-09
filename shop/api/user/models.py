from datetime import datetime

from shop.api.plugins import BaseModel, db, relationship, CRUDMixin
from shop.api.enums import AccountStatus


class User(db.Model, CRUDMixin, BaseModel):
    __tablename__ = 'user'
    name = db.Column('name', db.String(200))
    password = db.Column('password', db.String(200))
    email = db.Column('email', db.String(200))
    avatar = db.Column('avatar', db.String(256))
    last_login = db.Column('last_login', db.DateTime, default=datetime.utcnow)
    status = db.Column('status', db.Enum(AccountStatus))

    cart = db.relationship("Cart", backref=db.backref("cart_user"))
    address = db.relationship("Address", backref=db.backref("user_address"))

    def __init__(self, **kwargs):
        db.Model.__init__(self,
                          name=kwargs.get('name'),
                          password=kwargs.get('password'),
                          email=kwargs.get('email'),
                          status=kwargs.get('status') or AccountStatus.inactive,
                          last_login=kwargs.get('last_login') or datetime.utcnow(),
                          )

    def __str__(self):
        return


class Address(db.Model, CRUDMixin, BaseModel):
    __tablename__ = 'address'
    street = db.Column('street', db.String(200))
    city = db.Column('city', db.String(128))
    state = db.Column('state', db.String(200))
    zip_code = db.Column('zip_code', db.String(10))
    user_id = db.Column('user_id', db.ForeignKey('user.id'))

    user = relationship('User', backref=db.backref('user_address'))

    def __init__(self, **kwargs):
        db.Model.__init__(self,
                          street=kwargs.get('street'),
                          city=kwargs.get('city'),
                          state=kwargs.get('state'),
                          zip_code=kwargs.get('zip_code'),
                          user_id=kwargs.get('user_id') or None
                          )

    def __str__(self):
        return "ID=%d, City=%s, State=%d" % (self.id, self.city, self.state)
