from flask import Blueprint, request, jsonify
from flask import Flask, render_template, request, jsonify

users_bp = Blueprint('users', __name__)


# Liste des utilisateurs fictifs
users = [{"id": 1, "username": "admin", "password": "123"}]


@users_bp.route('/signup')
def signup():
   return render_template('signup.html')


# Route pour ajouter un utilisateur (Signup)
@users_bp.route('/signup', methods=['POST'])
def adduser():
    # Récupérer les données du formulaire
    # firstname = request.form['firstname']
    # name = request.form['name']
    username = request.form['username']
    password = request.form['password']
    # email = request.form['email']

    # Vérifier si le nom d'utilisateur existe déjà
    for user in users:
        if user['username'] == username:
            return jsonify({"msg": "Username already exists"}), 400
    
    # Ajouter l'utilisateur à la liste
    new_user = {"id": len(users) + 1,"username": username, "password": password}
    users.append(new_user)

    return jsonify({"msg": "User registered successfully"}), 201
