
from flask import Blueprint, jsonify, request

iot_bp = Blueprint('iot', __name__)
iot_data = []

@iot_bp.route('/', methods=['GET', 'POST'])
def manage_iot():
    if request.method == 'POST':
        record = request.json
        iot_data.append(record)
        return jsonify({'message': 'IoT data added', 'data': record}), 201
    return jsonify(iot_data)
