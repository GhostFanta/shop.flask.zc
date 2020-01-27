from flask import Blueprint, jsonify
from webargs import fields, ValidationError, flaskparser
from webargs.flaskparser import use_args

from http import HTTPStatus

shipment = Blueprint('shipment', __name__)
parser = flaskparser.FlaskParser()

parser.DEFAULT_VALIDATION_STATUS = 400
use_args = parser.use_args
