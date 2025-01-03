
from flask import Blueprint, request, jsonify
from db_utils import get_db_connection

biosafety_bp = Blueprint('biosafety', __name__)

@biosafety_bp.route('/', methods=['POST'])
def manage_biosafety():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        record = request.json
        cursor.execute("INSERT INTO biosafety (record) VALUES (?)", (str(record),))
        conn.commit()
        return jsonify({"message": "Biosafety record added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()
