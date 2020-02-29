from flask import Flask, jsonify, request
from flask_cors import CORS
import hashlib
import secrets

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)

USERS = []

@app.route('/register', methods=['GET', 'POST'])
def register():
    response_object = {
        'status': 'success',
    }
    post_data = request.get_json()
    if request.method == 'POST':
        token = hashlib.pbkdf2_hmac('sha256',secrets.token_bytes(), str.encode(request.headers.get('User-Agent')), 1000)
        USERS.append({
            'name': post_data.get('name'),
            'token': token.hex(),
        })
        response_object['name'] = post_data.get('name')
        response_object['token'] = token.hex()
    return response_object

@app.route('/auth', methods=['POST'])
def auth():
    response_object = {
        'status': 'success',
        'access': 'false'
    }
    post_data = request.get_json()
    token = post_data.get('token')
    for user in USERS:
        if token == user["token"]:
            response_object['access'] = 'true'
            response_object['name'] = user['name']
    return jsonify(response_object)

if __name__ == "__main__":
    app.run()
