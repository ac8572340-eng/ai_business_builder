from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    with open('index.html', 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/share')
def share():
    with open('share.html', 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/ai', methods=['POST'])
def ai():
    user_goal = request.json.get('goal', '')
    if not user_goal:
        return jsonify({'status': 'error'}), 400
    plan = f'Business Plan for {user_goal}'
    return jsonify({'status': 'success', 'data': plan})

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
