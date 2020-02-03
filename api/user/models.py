from datetime import datetime

from api.plugins import BaseModel, CRUDMixin, db, relationship
from api.enums import AccountStatus


class User(db.Model, BaseModel, CRUDMixin):
    __tablename__ = 'user'
    name = db.Column('name', db.String(200))
    password = db.Column('password', db.String(200))
    email = db.Column('email', db.String(200))
    avatar = db.Column('avatar', db.String(256))
    last_login = db.Column('last_login', db.DateTime, default=datetime.utcnow())
    status = db.Column('status', db.Enum(AccountStatus))

    cart = db.relationship("Cart", backref=db.backref("cart_user"))
    address = db.relationship("Address", backref=db.backref("user_address"))

    def __init__(self, **kwargs):
        self.__name = kwargs.get('name')
        self.__password = kwargs.get('password')
        self.__email = kwargs.get('email')
        self.__address = kwargs.get('address')
        self.__status = kwargs.get('status')
        self.__last_login = kwargs.get('last_login')

    def __str__(self):
        return "ID=%d, Name=%s, Email=%d" % (self.id, self.name, self.email)


class Address(db.Model, BaseModel, CRUDMixin):
    __tablename__ = 'address'
    street = db.Column('street', db.String(200))
    city = db.Column('city', db.String(128))
    state = db.Column('state', db.String(200))
    zip_code = db.Column('zip_code', db.String(10))
    user_id = db.Column('user_id', db.ForeignKey('user.id'))

    user = relationship('User', backref=db.backref('user_address'))

    def __init__(self, **kwargs):
        self.__street = kwargs.get('street')
        self.__city = kwargs.get('city')
        self.__state = kwargs.get('state')
        self.__zip_code = kwargs.get('zip_code')
        self.__country = kwargs.get('country')

    def __str__(self):
        return "ID=%d, City=%s, State=%d" % (self.id, self.city, self.state)
