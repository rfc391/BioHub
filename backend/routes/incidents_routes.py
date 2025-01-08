
# incidents_routes.py
from flask import Blueprint

incidents_bp = Blueprint('incidents', __name__)

@incidents_bp.route('/')
def index():
    return "This is the incidents route."
