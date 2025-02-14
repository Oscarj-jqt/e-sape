from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017")

# Sélection de la base de données et de la collection
db = client["e-sape_db"]
product_collection = db["products"]
user_collection = db["users"]

def insert_initial_data():
    products = [
        {"name": "Blouson Varsity brodé", "price": 5000, "description": "Ajoutez une touche de style à votre garde-robe avec ce blouson Varsity brodé. Parfait pour les journées fraîches, il combine confort et élégance. Son design moderne et ses détails brodés lui donnent un look unique et tendance.", "image": "https://fr.louisvuitton.com/images/is/image/lv/1/PP_VP_L/louis-vuitton-blouson-varsity-brode--HPL66ECAW622_PM2_Front%20view.jpg"},
        {"name": "Blouson varsity en cuir", "price": 5200, "description": "Un blouson classique revisité en cuir pour un style raffiné et intemporel. Son design Varsity combiné à la douceur du cuir offre un confort optimal et une allure élégante, parfait pour toutes les occasions.", "image": "https://fr.louisvuitton.com/images/is/image/lv/1/PP_VP_M/louis-vuitton--HPL68ECAW317_PM2_Front%20view.jpg?wid=750&hei=870"}
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



insert_initial_data()
