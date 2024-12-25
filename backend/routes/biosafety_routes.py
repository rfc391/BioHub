
from flask import Blueprint, jsonify, request

biosafety_bp = Blueprint('biosafety', __name__)
biosafety_data = []

@biosafety_bp.route('/', methods=['GET', 'POST'])
def manage_biosafety():
    if request.method == 'POST':
        record = request.json
        biosafety_data.append(record)
        return jsonify({'message': 'Biosafety record added', 'data': record}), 201
    return jsonify(biosafety_data)
