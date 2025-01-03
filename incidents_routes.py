
from flask import Blueprint, jsonify, request
import sqlite3

incidents_bp = Blueprint('incidents', __name__)
db_path = 'biohub.db'  # Path to the SQLite database

def get_db_connection():
    # Return a connection to the SQLite database.
    return sqlite3.connect(db_path)

@incidents_bp.route('/', methods=['GET', 'POST'])
def manage_incidents():
    if request.method == 'POST':
        record = request.json
        if not record:
            return jsonify({'error': 'Invalid data'}), 400

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO incidents (record) VALUES (?)", (str(record),))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Incidents record added', 'data': record}), 201

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM incidents")
    records = cursor.fetchall()
    conn.close()

    # Convert database rows to a list of dictionaries
    data = [{'id': row[0], 'record': row[1]} for row in records]
    return jsonify(data)
