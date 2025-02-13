from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson import ObjectId
from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["e-sape_db"]
collection = db["products"]

product_bp = Blueprint('products', __name__)


@product_bp.route('/products', methods=['GET'])
def get_products():
    products = list(collection.find({}, {"_id": 1, "name": 1, "price": 1}))
    
    # Transformer les ObjectId en string pour éviter les erreurs JSON
    for product in products:
        product["_id"] = str(product["_id"])

    return jsonify({"products": products}), 200

@product_bp.route('/admin/products', methods=['POST'])
@jwt_required()
def create_product():
    current_user = get_jwt_identity()
    if current_user != 'admin':
        return jsonify({"msg": "Accès refusé"}), 403

    data = request.get_json()
    if not data.get("name") or not data.get("price"):
        return jsonify({"msg": "Veuillez entrer un nom et un prix"}), 400

    new_product = {
        "name": data["name"].strip(),
        "price": data["price"]
    }
    
    # Vérifier si le produit existe déjà
    existing_product = collection.find_one({"name": new_product["name"]})
    if existing_product:
        return jsonify({"msg": f"Le produit '{new_product['name']}' existe déjà."}), 400

    result = collection.insert_one(new_product)
    new_product["_id"] = str(result.inserted_id)  # Convertir l'ObjectId en string

    return jsonify({"msg": "Produit créé", "product": new_product}), 201

from bson import ObjectId

@product_bp.route('/admin/products', methods=['PUT'])
@jwt_required()
def modify_product():
    print("🚀 Requête PUT reçue")  
    current_user = get_jwt_identity()
    
    if current_user != 'admin': 
        print("⛔ Accès refusé")
        return jsonify({"msg": "Accès refusé"}), 403

    data = request.get_json()
    print(f"📩 Données reçues: {data}")  


    try:
        object_id = ObjectId(data.get("id"))
        print(f"✅ ObjectId converti avec succès : {object_id}")
    except Exception as e:
        print(f"❌ Erreur conversion ObjectId: {e}")
        return jsonify({"msg": "ID invalide"}), 400


    product = collection.find_one({"_id": object_id})
    print(f"🔍 Produit trouvé dans la base : {product}")

    if not product:
        return jsonify({"msg": "Produit non trouvé"}), 404


    update_fields = {}
    if "name" in data:
        update_fields["name"] = data["name"]
    if "price" in data:
        update_fields["price"] = data["price"]

    if update_fields:
        collection.update_one({"_id": object_id}, {"$set": update_fields})
        print("✅ Produit mis à jour avec succès")
        return jsonify({"msg": "Produit modifié"}), 200
    else:
        return jsonify({"msg": "Aucune modification apportée"}), 400



@product_bp.route('/admin/products', methods=['DELETE'])
@jwt_required()
def delete_product():
    print("🚀 Requête DELETE reçue")  
    current_user = get_jwt_identity()
    
    if current_user != 'admin': 
        print(" Accès refusé")
        return jsonify({"msg": "Accès refusé"}), 403

    data = request.get_json()
    product_id = data.get("id")

    if not product_id:
        return jsonify({"msg": "ID du produit requis"}), 400

    # Convertir l'ID en ObjectId
    try:
        object_id = ObjectId(product_id)
        print(f" ObjectId converti avec succès : {object_id}")
    except Exception as e:
        print(f" Erreur conversion ObjectId: {e}")
        return jsonify({"msg": "ID invalide"}), 400

    # Vérifier si le produit existe
    existing_product = collection.find_one({"_id": object_id})
    print(f"🔍 Produit trouvé dans la base : {existing_product}")

    if not existing_product:
        return jsonify({"msg": "Produit non trouvé"}), 404

    # Supprimer le produit
    collection.delete_one({"_id": object_id})
    print(" Produit supprimé avec succès")

    return jsonify({"msg": "Produit supprimé"}), 200



# if __name__ == '__main__':
#     app.run(debug=True)
