from flask import Blueprint, jsonify
from webargs import fields, ValidationError, flaskparser
from webargs.flaskparser import use_args

from shop.api.shipment.models import Shipment, ShipmentTrack
from shop.api.exceptions import ShipmentExceptions

from http import HTTPStatus

shipment_blueprint = Blueprint('shipment', __name__)
parser = flaskparser.FlaskParser()

parser.DEFAULT_VALIDATION_STATUS = 400
use_args = parser.use_args


@shipment_blueprint.route('/shipments/<shipment_id>', methods=['GET'])
def get_shipment(shipment_id):
    shipment = Shipment.query.filter_by(shipment_id=shipment_id).first()
    if not shipment:
        return ShipmentExceptions.shipment_record_not_exist(), HTTPStatus.NOT_FOUND
    return


@shipment_blueprint.route('/shipments', methods=['POST'])
def create_shipment_record():
    pass


@shipment_blueprint.route('/shipments/<shipment_id>', methods=['PUT', 'PATCH'])
def update_shipment_record(shipment_id):
    pass


@shipment_blueprint.route('/shipments/<shipment_id>', methods=['DELETE'])
def delete_shipment_record(shipment_id):
    pass
