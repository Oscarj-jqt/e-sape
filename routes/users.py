from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

users_bp = Blueprint('users', __name__)

# Liste des utilisateurs fictifs
users = [{"id": 1, "username": "admin", "password": "123456"}]

# Liste des tokens invalidés (Blacklist)
blacklisted_tokens = set()

# Route pour afficher la page d'inscription
@users_bp.route('/signup')
def signup():
    return "Page d'inscription"

# Route pour ajouter un utilisateur (Signup)
@users_bp.route('/adduser', methods=['POST'])
def adduser():
    username = request.form['username']
    password = request.form['password']

    for user in users:
        if user['username'] == username:
            return jsonify({"msg": "Ce nom d'utilisateur existe déjà, prenez un autre"}), 400

    if len(password) < 6:
        return jsonify({"msg": "Le mot de passe doit être d'au moins 6 caractères"}), 400

    # Ajouter l'utilisateur à la liste
    new_user = {"id": len(users) + 1, "username": username, "password": password}
    users.append(new_user)

    return jsonify({"msg": "Utilisateur inscrit avec succès"}), 201

# Route de connexion (Login)
@users_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    for user in users:
        if user['username'] == username and user['password'] == password:
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
    
    return jsonify({"msg": "Mauvais identifiant ou mot de passe"}), 401

# Route de déconnexion (Blacklist du token)
@users_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    current_user = get_jwt_identity()
    blacklisted_tokens.add(current_user)  # Ajoute l'utilisateur à la liste des tokens invalidés
    return jsonify({"msg": "Déconnexion réussie"}), 200

# Route protégée (Test du token)
@users_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    if current_user in blacklisted_tokens:
        return jsonify({"msg": "Token invalide, veuillez vous reconnecter"}), 401

    return jsonify(logged_in_as=current_user), 200
