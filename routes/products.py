from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
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

@product_bp.route('/admin/products', methods=['PUT'])
@jwt_required()
def modify_product():
    current_user = get_jwt_identity()
    if current_user != 'admin':
        return jsonify({"msg": "Accès refusé"}), 403

    data = request.get_json()
    product_id = data.get("id")

    if not product_id:
        return jsonify({"msg": "ID du produit requis"}), 400

    # Vérifier si le produit existe
    existing_product = collection.find_one({"_id": product_id})
    if not existing_product:
        return jsonify({"msg": "Produit non trouvé"}), 404

    update_data = {}
    if "name" in data:
        update_data["name"] = data["name"]
    if "price" in data:
        update_data["price"] = data["price"]

    collection.update_one({"_id": product_id}, {"$set": update_data})

    return jsonify({"msg": "Produit modifié", "product": update_data}), 200


@product_bp.route('/admin/products', methods=['DELETE'])
@jwt_required()
def delete_product():
    current_user = get_jwt_identity()
    if current_user != 'admin':
        return jsonify({"msg": "Accès refusé"}), 403

    data = request.get_json()
    product_id = data.get("id")

    if not product_id:
        return jsonify({"msg": "ID du produit requis"}), 400

    # Vérifier si le produit existe
    existing_product = collection.find_one({"_id": product_id})
    if not existing_product:
        return jsonify({"msg": "Produit non trouvé"}), 404

    collection.delete_one({"_id": product_id})

    return jsonify({"msg": "Produit supprimé"}), 200


# if __name__ == '__main__':
#     app.run(debug=True)
