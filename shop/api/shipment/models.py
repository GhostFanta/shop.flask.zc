from shop.api.plugins import BaseModel, db, relationship
from shop.api.enums import ShipmentStatus
from shop.api.cart.models import Order


class Shipment(db.Model, BaseModel):
    __tablename__ = 'shipment'
    order_id = db.Column('order_id', db.ForeignKey('order.id'))
    shipment_status = db.Column('shipment_status', db.Enum(ShipmentStatus))

    def __init__(self, **kwargs):
        db.Model.__init__(self,
                          shipment_number=kwargs.get('shipment_number'),
                          shipment_status=kwargs.get('shipment_status'),
                          )


class ShipmentTrack(db.Model, BaseModel):
    __tablename__ = 'shipmenttrack'
    shipment_date = db.Column('shipment_date', db.Enum(ShipmentStatus))
    esitmated_arrival = db.Column('estimated_arrival', db.DateTime)
    track_number = db.Column('track_number', db.String(200))
    shipment_id = db.Column('shipment_id', db.ForeignKey('shipment.id'))

    shipment = relationship("Shipment", backref="shipmenttrack")

    def __init__(self, **kwargs):
        db.Model.__init__(self,
                          shipment_date=kwargs.get('shipment_date'),
                          estimated_arrival=kwargs.get('esitmated_arrival'),
                          track_number=kwargs.get('track_number')
                          )
