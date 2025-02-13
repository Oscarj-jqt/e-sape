from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017")

# Sélection de la base de données et de la collection
db = client["e-sape_db"]
product_collection = db["products"]
user_collection = db["users"]

def insert_initial_data():
    products = [
        {"name": "Produit A", "price": 20},
        {"name": "Produit B", "price": 30}
    ]
    
    for product in products:
        
        product_name = product["name"].strip()

        # Vérifier si un produit avec le même nom existe déjà
        existing_product = product_collection.find_one({"name": product_name})
        
        if not existing_product:
            # Insérer le produit si ce n'est pas le cas
            product_collection.insert_one(product)
            print(f"Donnée insérée : {product['name']}")
        else:
            print(f"Le produit {product['name']} existe déjà avec l'ID {existing_product['_id']}.")

    # Initialiser les utilisateurs
    users = [
        {"username": "admin", "password": "123456"}
    ]
    
    for user in users:
        username = user["username"].strip()

        # Vérifier si un utilisateur avec le même nom existe déjà
        existing_user = user_collection.find_one({"username": username})
        
        if not existing_user:
            # Insérer l'utilisateur si ce n'est pas le cas
            user_collection.insert_one(user)
            print(f"Utilisateur inséré : {user['username']}")
        else:
            print(f"L'utilisateur {user['username']} existe déjà avec l'ID {existing_user['_id']}.")




insert_initial_data()
