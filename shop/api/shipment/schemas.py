from marshmallow import Schema, fields


class ShipmentSchema(Schema):
    order_id = fields.Integer(attribute='id')


shipment_schema = ShipmentSchema()
