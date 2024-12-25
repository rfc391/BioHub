
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data storage for demonstration
data_store = {
    "biosafety": [],
    "biostasis": [],
    "iot_monitoring": [],
    "outbreaks": [],
    "incidents": [],
    "members": [],
    "projects": []
}

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to BioHub - Revolutionizing Biosafety and Monitoring!'})

# Member Management
@app.route('/members', methods=['GET', 'POST'])
def manage_members():
    if request.method == 'POST':
        member = request.json
        data_store['members'].append(member)
        return jsonify({'message': 'Member added!', 'data': member}), 201
    return jsonify(data_store['members'])

# Project Tracking
@app.route('/projects', methods=['GET', 'POST'])
def manage_projects():
    if request.method == 'POST':
        project = request.json
        data_store['projects'].append(project)
        return jsonify({'message': 'Project added!', 'data': project}), 201
    return jsonify(data_store['projects'])

# Compliance Checker
@app.route('/compliance/<member_id>', methods=['GET'])
def check_compliance(member_id):
    member = next((m for m in data_store['members'] if m.get('id') == member_id), None)
    if not member:
        return jsonify({'error': 'Member not found'}), 404
    
    # Example compliance check logic
    compliance_status = "Compliant" if member.get('profile_complete', False) else "Non-Compliant"
    return jsonify({'member_id': member_id, 'compliance_status': compliance_status})

if __name__ == '__main__':
    app.run(debug=True)

from backend.routes.biosafety_routes import biosafety_bp
from backend.routes.biostasis_routes import biostasis_bp
from backend.routes.iot_routes import iot_bp

app.register_blueprint(biosafety_bp, url_prefix='/biosafety')
app.register_blueprint(biostasis_bp, url_prefix='/biostasis')
app.register_blueprint(iot_bp, url_prefix='/iot-monitoring')

from backend.routes.outbreaks_routes import outbreaks_bp
from backend.routes.incidents_routes import incidents_bp

app.register_blueprint(outbreaks_bp, url_prefix='/outbreaks')
app.register_blueprint(incidents_bp, url_prefix='/incidents')

app.url_map.strict_slashes = False  # Disable strict slashes globally
