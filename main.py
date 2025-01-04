
from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields, ValidationError
from src.signal_processing import process_signal
from src.feature_extraction import extract_features
from src.ml_integration import predict_threats

# Initialize Flask app and Marshmallow for input validation
app = Flask(__name__)
ma = Marshmallow(app)


# Validation schema for input data
class SignalSchema(Schema):
    signal = fields.List(fields.Float(), required=True)


signal_schema = SignalSchema()


@app.route('/api/analyze', methods=['POST'])
def analyze_data():
    try:
        # Validate incoming data
        data = signal_schema.load(request.get_json())
        processed_data = process_signal(data['signal'])
        features = extract_features(processed_data)
        predictions = predict_threats(features)
        return jsonify({'predictions': predictions}), 200
    except ValidationError as ve:
        return jsonify({'error': 'Invalid input data', 'details': ve.messages}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
