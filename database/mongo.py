from pymongo import MongoClient

# Connexion sans authentification à MongoDB
client = MongoClient("mongodb://localhost:27017")

# Sélection de la base de données
db = client["e-sape_db"]

# Sélection de la collection
collection = db["products"]

# Insertion d'un document
collection.insert_one({"name": "Produit A", "price": 20})

print("Données insérées avec succès")
