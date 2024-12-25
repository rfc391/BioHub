
from flask import Blueprint, jsonify, request

incidents_bp = Blueprint('incidents', __name__, url_prefix='/incidents')
incidents_data = []

@incidents_bp.route('/', methods=['GET', 'POST'])
def manage_incidents():
    if request.method == 'POST':
        record = request.json
        incidents_data.append(record)
        return jsonify({'message': 'Incident reported', 'data': record}), 201
    return jsonify(incidents_data)
