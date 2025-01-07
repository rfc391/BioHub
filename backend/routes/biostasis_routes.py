
# biostasis_routes.py
from flask import Blueprint

biostasis_bp = Blueprint('biostasis', __name__)

@biostasis_bp.route('/')
def index():
    return "This is the biostasis route."
