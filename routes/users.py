from flask import Blueprint, request, jsonify

users_bp = Blueprint('users', __name__)


# Liste des utilisateurs fictifs
users = [{"id": 1, "username": "admin", "password": "123"}]

# Route pour ajouter un utilisateur (Signup)
@users_bp.route('/signup', methods=['POST'])
def signup():
    # Récupérer les données du formulaire
    firstname = request.form['firstname']
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    # Vérifier si le nom d'utilisateur existe déjà
    for user in users:
        if user['username'] == username:
            return jsonify({"msg": "Username already exists"}), 400
    
    # Ajouter l'utilisateur à la liste
    new_user = {"id": len(users) + 1, "firstname": firstname, "name": name, "username": username, "password": password, "email": email}
    users.append(new_user)

    return jsonify({"msg": "User registered successfully"}), 201
