from flask import Flask, Blueprint, render_template, request, jsonify

users_bp = Blueprint('users', __name__)


# Liste des utilisateurs fictifs
users = [{"id": 1, "username": "admin", "password": "123456"}]


@users_bp.route('/signup')
def signup():
   return render_template('signup.html')


# Route pour ajouter un utilisateur (Signup)
@users_bp.route('/adduser', methods=['POST'])
def adduser():

    username = request.form['username']
    password = request.form['password']

    for user in users:
        if user['username'] == username:
            return "Ce nom d'utilisateur existe déjà, prennez un autre", 400
        
    if len(password) < 6:
        return "Le mot de passe doit être d'au moins 6 caractères", 400    
    
    # Ajouter l'utilisateur à la liste
    new_user = {"id": len(users) + 1,"username": username, "password": password}
    users.append(new_user)

    return "User registered successfully" , 201
