from enum import Enum


class OrderStatus(Enum):
    pending = 'pending'
    unshipped = 'unshipped'
    shipped = 'shipped'
    completed = 'completed'
    canceled = 'canceled'


class AccountStatus(Enum):
    active = 'active'
    inactive = 'inactive'
    suspended = 'suspended'


class ShipmentStatus(Enum):
    pending = 'pending'
    shipped = 'shipped'
    delivered = 'delivered'
    on_hold = 'on_hold'
    received = 'received'


class Roles(Enum):
    admin = 'admin'
    member = 'member'
