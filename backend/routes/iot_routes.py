
# iot_routes.py
from flask import Blueprint

iot_bp = Blueprint('iot', __name__)

@iot_bp.route('/')
def index():
    return "This is the iot route."
