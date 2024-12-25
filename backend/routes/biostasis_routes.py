
from flask import Blueprint, jsonify, request

biostasis_bp = Blueprint('biostasis', __name__)
biostasis_data = []

@biostasis_bp.route('/', methods=['GET', 'POST'])
def manage_biostasis():
    if request.method == 'POST':
        record = request.json
        biostasis_data.append(record)
        return jsonify({'message': 'Biostasis record added', 'data': record}), 201
    return jsonify(biostasis_data)
