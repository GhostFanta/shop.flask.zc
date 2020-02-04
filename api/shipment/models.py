from api.plugins import BaseModel, db
from api.enums import ShipmentStatus


class Shipment(db.Model, BaseModel):
    __tablename__ = 'shipment'
    shipment_number = db.Column('shipment_number', db.ForeignKey('shipmenttrack.id'))
    # shipment_number = db.Column('shipment_number', db.Integer)
    shipment_status = db.Column('shipment_status', db.Enum(ShipmentStatus))

    def __init__(self, **kwargs):
        self.__shipment_number = kwargs.get('shipment_number')
        self.__shipment_status = kwargs.get('shipment_status')


class ShipmentTrack(db.Model, BaseModel):
    __tablename__ = 'shipmenttrack'
    shipment_date = db.Column('shipment_date', db.Enum(ShipmentStatus))
    esitmated_arrival = db.Column('estimated_arrival', db.DateTime)
    track_number = db.Column('track_number', db.String(200))

    shipment = db.relationship("Shipment", backref="shipmenttrack")

    def __init__(self, **kwargs):
        self.__shipment_date = kwargs.get('shipment_date')
        self.__estimated_arrival = kwargs.get('esitmated_arrival')
        self.__track_number = kwargs.get('track_number')
