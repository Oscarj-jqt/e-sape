from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity




product_bp = Blueprint('products', __name__)


# Liste des produits fictifs
products = [{"id": 1, "name": "Produit A", "price": 20},
             {"id": 2, "name": "Produit B", "price": 25}
            ]

@product_bp.route('/products', methods=['GET'])
def get_products(): 
    return jsonify({"Les produits": products}), 200


@product_bp.route('/admin/products', methods=['POST'])
@jwt_required()
def create_product():
    current_user = get_jwt_identity()  
    if current_user != 'admin':  
        return jsonify({"msg": "Accès refusé"}), 403

    data = request.get_json()
    if not data.get("name") or not data.get("price"):
        return jsonify({"msg": "Veuillez à mettre un nom et un prix au produit"}), 400

    new_product = {
        "id": len(products) + 1,
        "name": data["name"],
        "price": data["price"]
    }
    products.append(new_product)
    return jsonify({"msg": "Produit créé", "product": new_product}), 201

@product_bp.route('/admin/products', methods=['PUT'])
@jwt_required()
def modify_product():
    current_user = get_jwt_identity()  
    if current_user != 'admin': 
        return jsonify({"msg": "Accès refusé"}), 403

    data = request.get_json()
    product_id = data.get("id")
    product = next((prod for prod in products if prod["id"] == product_id), None)

    if not product:
        return jsonify({"msg": "Produit non trouvé"}), 404

    product["name"] = data.get("name", product["name"])
    product["price"] = data.get("price", product["price"])
    
    return jsonify({"msg": "Produit modifié", "product": product}), 200

@product_bp.route('/admin/products', methods=['DELETE'])
@jwt_required()
def delete_product():
    current_user = get_jwt_identity()  
    if current_user != 'admin': 
        return jsonify({"msg": "Accès refusé"}), 403

    data = request.get_json()
    product_id = data.get("id")
    product = next((prod for prod in products if prod["id"] == product_id), None)

    if not product:
        return jsonify({"msg": "Produit non trouvé"}), 404

    products.remove(product)
    
    return jsonify({"msg": "Produit supprimé"}), 200

# if __name__ == '__main__':
#     app.run(debug=True)
