from flask import Flask, jsonify, request
import json

app = Flask(__name__)

USERS_FILE = 'users.json'

def read_users():
    with open(USERS_FILE, 'r') as file:
        return json.load(file)

def write_users(users):
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file, indent=4)

@app.route('/users', methods=['GET'])
def get_users():
    users = read_users()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()

    users = read_users()

    new_user['id'] = users[-1]['id'] + 1 if users else 1

    users.append(new_user)

    write_users(users)

    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)
