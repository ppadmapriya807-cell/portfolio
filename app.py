"""
==============================================
  Padmapriya R - Portfolio Website Backend
  Flask Application - Windows Compatible
  Uses PyMySQL (no C++ compiler needed!)
==============================================
"""

from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import pymysql
import os
import re
from datetime import datetime
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# ── App Initialization ─────────────────────────────────────────
app = Flask(__name__)
CORS(app)
app.secret_key = os.environ.get('SECRET_KEY', 'padmapriya-portfolio-secret')

# ── Database Configuration ─────────────────────────────────────
DB_CONFIG = {
    'host':     os.environ.get('MYSQL_HOST', 'localhost'),
    'user':     os.environ.get('MYSQL_USER', 'root'),
    'password': os.environ.get('MYSQL_PASSWORD', ''),
    'database': os.environ.get('MYSQL_DB', 'portfolio_db'),
    'port':     int(os.environ.get('MYSQL_PORT', 3306)),
    'charset':  'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

def get_db():
    """Create and return a new database connection."""
    return pymysql.connect(**DB_CONFIG)

# ── Helper: Validate Email ─────────────────────────────────────
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None

# ── Routes ─────────────────────────────────────────────────────

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact', methods=['POST'])
def contact():
    try:
        data    = request.get_json()
        name    = data.get('name', '').strip()
        email   = data.get('email', '').strip()
        message = data.get('message', '').strip()

        # Validation
        if not name or not email or not message:
            return jsonify({'success': False, 'message': 'All fields are required.'}), 400
        if len(name) < 2:
            return jsonify({'success': False, 'message': 'Name must be at least 2 characters.'}), 400
        if not is_valid_email(email):
            return jsonify({'success': False, 'message': 'Please enter a valid email address.'}), 400
        if len(message) < 10:
            return jsonify({'success': False, 'message': 'Message must be at least 10 characters.'}), 400

        # Save to database
        conn   = get_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO contacts (name, email, message, submitted_at) VALUES (%s, %s, %s, %s)",
            (name, email, message, datetime.now())
        )
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({
            'success': True,
            'message': f"Thank you, {name}! Your message has been received. I'll get back to you soon."
        }), 200

    except Exception as e:
        print(f"[ERROR] {e}")
        return jsonify({'success': False, 'message': 'Server error. Please try again later.'}), 500


@app.route('/resume')
def resume():
    try:
        return send_from_directory(
            directory=os.path.join(app.root_path, 'static'),
            path='Padmapriya_R_Resume.pdf',
            as_attachment=True
        )
    except Exception:
        return jsonify({'error': 'Resume file not found.'}), 404


@app.route('/health')
def health():
    return jsonify({'status': 'ok'}), 200


@app.errorhandler(404)
def not_found(e):
    return render_template('index.html'), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
