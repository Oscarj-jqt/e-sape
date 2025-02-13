import graphene
from database.mongo import product_collection
from database.mongo import user_collection



# Définition de la classe Product pour GraphQL
class Product(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    price = graphene.Float()

class User(graphene.ObjectType):
    id = graphene.String()
    username = graphene.String()
    password = graphene.String()

#Affichage des données
class Query(graphene.ObjectType):
    products = graphene.List(Product)
    users = graphene.List(User)


    def resolve_products(self, info):
        # Récupérer tous les produits de MongoDB
        products = product_collection.find()
        return [
            Product(id=product['_id'], name=product['name'], price=product['price'])
            for product in products
        ]
    
    def resolve_users(self, info):
        # Récupérer tous les utilisateurs de MongoDB
        users = user_collection.find({"username": {"$exists": True}})
        return [
            User(id=str(user['_id']), username=user['username'], password=user['password'])
            for user in users
        ]
    
class Mutation(graphene.ObjectType):
    create_user = graphene.Field(User, username=graphene.String(), password=graphene.String())

    def resolve_create_user(self, info, username, password):
        # Ajouter un utilisateur à MongoDB
        if len(password) < 6:
            raise Exception("Le mot de passe doit être d'au moins 6 caractères.")
        
        # Vérifier si le nom d'utilisateur existe déjà
        if user_collection.find_one({"username": username}):
            raise Exception("Ce nom d'utilisateur existe déjà.")
        
        # Insérer l'utilisateur dans la base de données MongoDB
        new_user = {"username": username, "password": password}
        result = user_collection.insert_one(new_user)
        
        return User(id=str(result.inserted_id), username=username, password=password)


# Création du schéma GraphQL
schema = graphene.Schema(query=Query, mutation=Mutation)
