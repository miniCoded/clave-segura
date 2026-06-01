from flask import Flask, request, jsonify
from flask_cors import CORS
from password_validator import PasswordValidator

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

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
