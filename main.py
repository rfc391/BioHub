
from flask import Flask, jsonify, request
from backend_organized.core.mock_global_database_handler import MockGlobalDatabaseHandler
from backend_organized.core.security_module import SecurityModule

app = Flask(__name__)

# Initialize Handlers
mock_global_db_handler = MockGlobalDatabaseHandler()
security = SecurityModule()

# Endpoint to fetch data from mock global databases
@app.route("/api/global-data/<database_name>", methods=["GET"])
def fetch_mock_global_data(database_name):
    endpoint = request.args.get("endpoint", "")
    params = request.args.to_dict(flat=True)
    params.pop("endpoint", None)  # Remove 'endpoint' from parameters
    try:
        data = mock_global_db_handler.fetch_data(database_name, endpoint, params)
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

# Security Module Routes
@app.route("/api/security/hash", methods=["POST"])
def hash_data():
    data = request.json.get("data", "")
    if not data:
        return jsonify({"error": "No data provided"}), 400
    hashed = security.hash_data(data)
    return jsonify({"hashed_data": hashed})

@app.route("/api/security/encrypt", methods=["POST"])
def encrypt_data():
    data = request.json.get("data", "")
    if not data:
        return jsonify({"error": "No data provided"}), 400
    encrypted = security.encrypt_data(data)
    return jsonify({"encrypted_data": encrypted})

@app.route("/api/security/decrypt", methods=["POST"])
def decrypt_data():
    encrypted_data = request.json.get("encrypted_data", "")
    if not encrypted_data:
        return jsonify({"error": "No encrypted data provided"}), 400
    try:
        decrypted = security.decrypt_data(encrypted_data)
        return jsonify({"decrypted_data": decrypted})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
