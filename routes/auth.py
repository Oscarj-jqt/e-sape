from flask import Blueprint, request, jsonify
from flask import Flask, render_template, request, jsonify
from flask_jwt_extended import create_access_token
import bcrypt

auth_bp = Blueprint('auth', __name__)

hashed_password = bcrypt.hashpw("123".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Liste des utilisateurs fictifs
users = [{"id": 1, "username": "admin", "password": hashed_password}]

@auth_bp.route('/login')
def login():
   return render_template('login.html')

# Route de login pour générer un token JWT
@auth_bp.route('/login', methods=["POST"])
def check_login():
    username = request.form.get('username')
    password = request.form.get('password')

    for user in users:
        if user['username'] == username and user['password'] == password:
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token)
    return jsonify({"msg": "Bad username or password"}), 401
