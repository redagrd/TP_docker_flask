# CRUD pour gérer les utilisateurs

import flask
from flask import request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS

# creation de l'app flask
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# configuration de la base de données
app.config["MONGO_URI"] = "mongodb://localhost:27017/users"
mongo = PyMongo(app)

# configuration de CORS
CORS(app)

# route pour afficher tous les utilisateurs
@app.route('/users', methods=['GET'])
def get_all_users():
    users = mongo.db.users.find()
    result = []
    for user in users:
        result.append({'_id': str(user['_id']), 'name': user['name'], 'email': user['email']})
    return jsonify(result)

# route pour afficher un utilisateur
@app.route('/users/<id>', methods=['GET'])
def get_one_user(id):
    user = mongo.db.users.find_one({'_id': ObjectId(id)})
    result = {'_id': str(user['_id']), 'name': user['name'], 'email': user['email']}
    return jsonify(result)

# route pour ajouter un utilisateur
@app.route('/users', methods=['POST'])
def add_user():
    user = mongo.db.users
    name = request.json['name']
    email = request.json['email']
    user_id = user.insert({'name': name, 'email': email})
    new_user = user.find_one({'_id': user_id})
    result = {'_id': str(new_user['_id']), 'name': new_user['name'], 'email': new_user['email']}
    return jsonify(result)

# route pour modifier un utilisateur
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    user = mongo.db.users
    name = request.json['name']
    email = request.json['email']
    user_id = user.update_one({'_id': ObjectId(id)}, {'$set': {'name': name, 'email': email}})
    updated_user = user.find_one({'_id': ObjectId(id)})
    result = {'_id': str(updated_user['_id']), 'name': updated_user['name'], 'email': updated_user['email']}
    return jsonify(result)

# route pour supprimer un utilisateur
@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    user = mongo.db.users
    user_id = user.delete_one({'_id': ObjectId(id)})
    result = {'message': 'User deleted successfully'}
    return jsonify(result)

# lancement de l'app flask
if __name__ == '__main__':
    app.run()
