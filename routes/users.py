from flask import Flask, Blueprint, render_template, request, jsonify
from database.mongo import product_collection
from database.mongo import user_collection

users_bp = Blueprint('users', __name__)


# Liste des utilisateurs fictifs
users = [{"id": 1, "username": "admin", "password": "123456"}]


@users_bp.route('/signup')
def signup():
   return render_template('signup.html')


# Route pour ajouter un  utilisateur (Signup)
@users_bp.route('/adduser', methods=['POST'])
def adduser():
    username = request.form['username']
    password = request.form['password']

    # Vérification de l'existence de l'utilisateur
    if user_collection.find_one({"username": username}):
        return "Ce nom d'utilisateur existe déjà, prennez un autre", 400

    # Vérification de la longueur du mot de passe
    if len(password) < 6:
        return "Le mot de passe doit être d'au moins 6 caractères", 400    
    
    # Ajouter l'utilisateur à MongoDB
    new_user = {"username": username, "password": password}
    user_collection.insert_one(new_user)

    return "User registered successfully", 201
