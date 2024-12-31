
from flask import Flask, jsonify
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

@app.route('/api/status')
def get_status():
    return jsonify({"status": "operational"})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
