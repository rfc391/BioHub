
from flask import Flask, jsonify
from backend.routes.biosafety_routes import biosafety_bp
from backend.routes.biostasis_routes import biostasis_bp
from backend.routes.iot_routes import iot_bp
from backend.routes.outbreaks_routes import outbreaks_bp
from backend.routes.incidents_routes import incidents_bp

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to BioHub - Revolutionizing Biosafety and Monitoring!'})

# Register Blueprints
app.register_blueprint(biosafety_bp, url_prefix='/biosafety')
app.register_blueprint(biostasis_bp, url_prefix='/biostasis')
app.register_blueprint(iot_bp, url_prefix='/iot-monitoring')
app.register_blueprint(outbreaks_bp, url_prefix='/outbreaks')
app.register_blueprint(incidents_bp, url_prefix='/incidents')

app.url_map.strict_slashes = False  # Disable strict slashes globally

import os

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(debug=debug_mode)
