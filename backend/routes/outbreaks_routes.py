
from flask import Blueprint, jsonify, request

outbreaks_bp = Blueprint('outbreaks', __name__, url_prefix='/outbreaks')
outbreaks_data = []

@outbreaks_bp.route('/', methods=['GET', 'POST'])
def manage_outbreaks():
    if request.method == 'POST':
        record = request.json
        outbreaks_data.append(record)
        return jsonify({'message': 'Outbreak added', 'data': record}), 201
    return jsonify(outbreaks_data)
