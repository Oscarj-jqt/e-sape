from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import create_access_token
from pymongo import MongoClient
import logging
import os

auth_bp = Blueprint('auth', __name__)

# Connexion à MongoDB (modifie l'URI selon ton environnement)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["e-sape_db"] 
users_collection = db["users"]

# Traçage des tentatives de connexion
logging.basicConfig(level=logging.INFO)

# Liste des utilisateurs fictifs avec mot de passe en clair
# users = [{"id": 1, "username": "admin", "password": "123456"}]

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

    # Recherche de l'utilisateur dans MongoDB avec un mot de passe en clair
    user = users_collection.find_one({"username": username, "password": password})

    if user:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)

    return jsonify({"msg": "Bad username or password"}), 401


# # Route de déconnexion (Blacklist du token)
# @users_bp.route('/logout', methods=['POST'])
# @jwt_required()
# def logout():
#     current_user = get_jwt_identity()
#     blacklisted_tokens.add(current_user)  # Ajoute l'utilisateur à la liste des tokens invalidés
#     return jsonify({"msg": "Déconnexion réussie"}), 200
