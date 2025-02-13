from flask import Flask, jsonify, request, abort
from flask_restx import Api, Resource, fields
import json
import os

app = Flask(__name__)
api = Api(app, title="User Management API", version="1.0", description="API para gerenciar usuários usando JSON como banco de dados")

USERS_FILE = 'users.json'

def read_users():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'w') as file:
            json.dump([], file)
        return []
    with open(USERS_FILE, 'r') as file:
        return json.load(file)

def write_users(users):
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file, indent=4)

def find_user_by_id(user_id):
    users = read_users()
    return next((user for user in users if user['id'] == user_id), None)

user_model = api.model('User', {
    'id': fields.Integer(description='ID do Usuário', readonly=True),
    'name': fields.String(required=True, description='Nome do Usuário'),
    'email': fields.String(required=True, description='Email do Usuário')
})

@api.route('/users')
class UserList(Resource):
    @api.doc('list_users', responses={200: 'Lista de usuários retornada com sucesso.'})
    def get(self):
        """Retorna todos os usuários"""
        users = read_users()
        return jsonify(users)

    @api.doc('create_user', responses={201: 'Usuário criado com sucesso.', 400: 'Email já cadastrado.'})
    @api.expect(user_model)
    def post(self):
        """Adiciona um novo usuário"""
        new_user = request.get_json()

        users = read_users()
        if any(user['email'] == new_user['email'] for user in users):
            abort(400, description="Email já cadastrado.")

        new_user['id'] = users[-1]['id'] + 1 if users else 1
        users.append(new_user)
        write_users(users)

        return jsonify(new_user), 201

@api.route('/users/<int:user_id>')
class UserResource(Resource):
    @api.doc('get_user', responses={200: 'Usuário encontrado.', 404: 'Usuário não encontrado.'})
    def get(self, user_id):
        """Retorna um usuário específico"""
        user = find_user_by_id(user_id)
        if user is None:
            abort(404, description="Usuário não encontrado.")
        return jsonify(user)

    @api.doc('update_user', responses={200: 'Usuário atualizado.', 404: 'Usuário não encontrado.'})
    @api.expect(user_model)
    def put(self, user_id):
        """Atualiza um usuário específico"""
        user_data = request.get_json()
        users = read_users()
        user = find_user_by_id(user_id)
        if user is None:
            abort(404, description="Usuário não encontrado.")

        user.update(user_data)
        write_users(users)
        return jsonify(user)

    @api.doc('delete_user', responses={204: 'Usuário deletado.', 404: 'Usuário não encontrado.'})
    def delete(self, user_id):
        """Deleta um usuário específico"""
        users = read_users()
        user = find_user_by_id(user_id)
        if user is None:
            abort(404, description="Usuário não encontrado.")

        users.remove(user)
        write_users(users)
        return '', 204

if __name__ == '__main__':
    app.run(debug=True)