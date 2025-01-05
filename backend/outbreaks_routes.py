
from flask import Blueprint, jsonify, request
import sqlite3

outbreaks_bp = Blueprint('outbreaks', __name__)
db_path = 'biohub.db'  # Path to the SQLite database

def get_db_connection():
    # Return a connection to the SQLite database.
    return sqlite3.connect(db_path)

@outbreaks_bp.route('/', methods=['GET', 'POST'])
def manage_outbreaks():
    if request.method == 'POST':
        record = request.json
        if not record:
            return jsonify({'error': 'Invalid data'}), 400

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO outbreaks (record) VALUES (?)", (str(record),))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Outbreaks record added', 'data': record}), 201

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM outbreaks")
    records = cursor.fetchall()
    conn.close()

    # Convert database rows to a list of dictionaries
    data = [{'id': row[0], 'record': row[1]} for row in records]
    return jsonify(data)
