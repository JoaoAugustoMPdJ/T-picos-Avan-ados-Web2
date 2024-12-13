from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields
import json

app = Flask(__name__)
api = Api(app, title="User Management API", version="1.0", description="API para gerenciar usuários usando JSON como banco de dados")

USERS_FILE = 'users.json'

def read_users():
    with open(USERS_FILE, 'r') as file:
        return json.load(file)

def write_users(users):
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file, indent=4)

user_model = api.model('User', {
    'id': fields.Integer(description='ID do Usuário', readonly=True),
    'name': fields.String(required=True, description='Nome do Usuário'),
    'email': fields.String(required=True, description='Email do Usuário')
})

@api.route('/users')
class UserList(Resource):
    @api.doc('list_users')
    @api.response(200, 'Lista de usuários retornada com sucesso.')
    def get(self):
        """Retorna todos os usuários"""
        users = read_users()
        return jsonify(users)

    @api.doc('create_user')
    @api.expect(user_model)
    @api.response(201, 'Usuário criado com sucesso.')
    def post(self):
        """Adiciona um novo usuário"""
        new_user = request.get_json()

        users = read_users()
        new_user['id'] = users[-1]['id'] + 1 if users else 1

        users.append(new_user)
        write_users(users)

        return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)
