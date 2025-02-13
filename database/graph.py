import graphene
from database.mongo import collection


# Définition de la classe Product pour GraphQL
class Product(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    price = graphene.Float()


class Query(graphene.ObjectType):
    products = graphene.List(Product)

    def resolve_products(self, info):
        # Récupérer tous les produits de MongoDB
        products = collection.find()
        return [
            Product(id=product['_id'], name=product['name'], price=product['price'])
            for product in products
        ]

# Création du schéma GraphQL
schema = graphene.Schema(query=Query)
