
# outbreaks_routes.py
from flask import Blueprint

outbreaks_bp = Blueprint('outbreaks', __name__)

@outbreaks_bp.route('/')
def index():
    return "This is the outbreaks route."
