from flask import Flask, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

app = Flask(__name__)

# Liste des produits fictifs
products = [{"id": 1, "name": "Produit A", "price": 20},
             {"id": 2, "name": "Produit B", "price": 25}
            ]

@app.route('/product', methods=['GET'])
@jwt_required()
def get_products():
    # Récupération de l'identité avec le token
    current_user = get_jwt_identity()  
    if current_user != 'admin':
        # Si ce n'est pas l'admin
        return jsonify({"msg": "Accès refusé"}), 403

    return jsonify({"products": products}), 200


@app.route('/admin/product', methods=['POST'])
@jwt_required()
def create_product():
    current_user = get_jwt_identity()  
    if current_user != 'admin':  # Vérifier si l'utilisateur est admin
        return jsonify({"msg": "Access forbidden: admin only"}), 403

    data = request.get_json()
    if not data.get("name") or not data.get("price"):
        return jsonify({"msg": "Veuillez à mettre un nom et un prix au produit"}), 400

    new_product = {
        "id": len(products) + 1,
        "name": data["name"],
        "price": data["price"]
    }
    products.append(new_product)
    return jsonify({"msg": "Product created", "product": new_product}), 201

@app.route('/admin/product', methods=['PUT'])
@jwt_required()
def modify_product():
    current_user = get_jwt_identity()  
    if current_user != 'admin':  # Vérifier si l'utilisateur est admin
        return jsonify({"msg": "Access forbidden: admin only"}), 403

    data = request.get_json()
    product_id = data.get("id")
    product = next((prod for prod in products if prod["id"] == product_id), None)

    if not product:
        return jsonify({"msg": "Product not found"}), 404

    product["name"] = data.get("name", product["name"])
    product["price"] = data.get("price", product["price"])
    
    return jsonify({"msg": "Product modified", "product": product}), 200

@app.route('/admin/product', methods=['DELETE'])
@jwt_required()
def delete_product():
    current_user = get_jwt_identity()  
<<<<<<< HEAD
    if current_user != 'admin': 
=======
    if current_user != 'admin':  # Vérifier si l'utilisateur est admin
>>>>>>> 746ce55fdf485f1351caa09a1f5715d5cf153552
        return jsonify({"msg": "Access forbidden: admin only"}), 403

    data = request.get_json()
    product_id = data.get("id")
    product = next((prod for prod in products if prod["id"] == product_id), None)

    if not product:
        return jsonify({"msg": "Product not found"}), 404

    products.remove(product)
    
    return jsonify({"msg": "Product deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
