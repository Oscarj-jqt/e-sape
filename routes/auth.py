from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import create_access_token
import bcrypt
import logging

auth_bp = Blueprint('auth', __name__)

# Traçage des tentatives de connexion
logging.basicConfig(level=logging.INFO)

# Liste des utilisateurs fictifs avec mot de passe en clair
users = [{"id": 1, "username": "admin", "password": "123456"}]

@auth_bp.route('/login')
def login():
    return render_template('login.html')

# Route de login pour générer un token JWT
@auth_bp.route('/login', methods=["POST"])
def check_login():
    data = request.get_json(silent=True)  # Récupère les données JSON
    if not data:
        # logging.debug("Aucune donnée reçue")
        # return jsonify({"msg": "Missing JSON in request"}), 400
        data = request.form

    username = data.get("username")
    password = data.get("password")

    logging.debug(f"Tentative de connexion avec username: {username}, password: {password}")

    for user in users:
        # Vérification du mot de passe en clair
        if user["username"] == username and user["password"] == password:
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token)

    return jsonify({"msg": "Bad username or password"}), 401
