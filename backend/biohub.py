
import sqlite3
from flask import Flask, jsonify, request
from backend.routes.biosafety_routes import biosafety_bp
from backend.routes.biostasis_routes import biostasis_bp
from backend.routes.iot_routes import iot_bp
from backend.routes.outbreaks_routes import outbreaks_bp
from backend.routes.incidents_routes import incidents_bp

app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('biohub.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to BioHub - Revolutionizing Biosafety and Monitoring!'})

# Register Blueprints
app.register_blueprint(biosafety_bp, url_prefix='/biosafety')
app.register_blueprint(biostasis_bp, url_prefix='/biostasis')
app.register_blueprint(iot_bp, url_prefix='/iot-monitoring')
app.register_blueprint(outbreaks_bp, url_prefix='/outbreaks')
app.register_blueprint(incidents_bp, url_prefix='/incidents')

if __name__ == '__main__':
    app.run(debug=True)
