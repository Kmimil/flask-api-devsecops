import flask
from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)
@app.route('/')
def home():
    return jsonify({
        "message": "Hello, World! Notre API DevSecOps est opérationnelle!",
        "version": "1.0.0",
        "environment": os.getenv('ENVIRONMENT', 'development'),
        "timestamp": datetime.now().isoformat()
    })
@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "service": "Flask API",
        "timestamp": datetime.now().isoformat()
    })
@app.route('/info')
def info():
    return jsonify({
        "service": "API Flask - TP DevSecOps",
        "institution": "ENSAJ - CCN",
        "features": [
            "CI/CD Automatisé",
            "Scan de sécurité",
            "Déploiement AWS",
            "Validation DevSecOps"
        ]
    })
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
