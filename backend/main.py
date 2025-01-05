
from flask import Flask, jsonify
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)
    load_dotenv()

    @app.route('/api/status')
    def get_status():
        return jsonify({
            "status": "operational",
            "version": "1.0.0"
        })

    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.getenv('PORT', 3000))
    app.run(host='0.0.0.0', port=port, debug=False)
