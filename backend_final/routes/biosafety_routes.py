
# biosafety_routes.py
from flask import Blueprint

biosafety_bp = Blueprint('biosafety', __name__)

@biosafety_bp.route('/')
def index():
    return "This is the biosafety route."
