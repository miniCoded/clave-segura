from flask import Flask, request, jsonify
from flask_cors import CORS
from password_validator import PasswordValidator
import random
import string

app = Flask(__name__)
CORS(app)

@app.route('/api/validate-password', methods=['POST'])
def validate_password():
    """Validate password and return security level."""
    data = request.json
    password = data.get('password', '')
    
    if not password:
        return jsonify({
            'security_level': 'unsafe',
            'message': 'Password cannot be empty',
            'details': {}
        }), 200
    
    security_level, details = PasswordValidator.validate(password)
    
    return jsonify({
        'security_level': security_level,
        'message': f'Password is {security_level}',
        'details': details
    }), 200

@app.route('/api/generate-password', methods=['POST'])
def generate_password():
    """Generate a secure password from a word."""
    data = request.json
    word = data.get('word', '')
    
    if not word or len(word.strip()) == 0:
        return jsonify({
            'security_level': 'unsafe',
            'message': 'Word cannot be empty',
            'details': {}
        }), 200
    
    # Generate password using the PasswordValidator class
    password, details = PasswordValidator.generate_from_word(word)
    
    return jsonify({
        'security_level': details.get('complexity_met', False) and not details.get('has_obvious_patterns', True) and len(password) >= 12 and 'secure' or 'half-secure',
        'message': f'Generated password: {password}',
        'details': details
    }), 200

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=5000)
