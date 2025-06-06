from flask import Flask
from flask import Flask, render_template, request, jsonify
from flask_jwt_extended import JWTManager
from routes.auth import auth_bp 
from routes.users import users_bp
from routes.products import product_bp
from datetime import timedelta
from flask_pymongo import PyMongo
from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from database.graph import schema



app = Flask(__name__)
# liaison back(flask) et front(react)
CORS(app, resources={r"/products": {"origins": "http://localhost:3000"},
     r"/login": {"origins": "http://localhost:3000"},
    r"/signup": {"origins": "http://localhost:3000"},
    r"/admin/*": {"origins": "http://localhost:3000"}})

# API GraphQL pour tout gérer en 1 route au lieu de REST
app.add_url_rule("/graphql", view_func=GraphQLView.as_view(
   "graphql",
   schema=schema,
   graphiql=True 
))

# Configuration MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/e-sape_db"
mongo = PyMongo(app)

# Configuration de la clé JWT
app.config['JWT_SECRET_KEY'] = 'web2'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)  
jwt = JWTManager(app)

# Enregistrement des Blueprints
app.register_blueprint(auth_bp) 
app.register_blueprint(product_bp)  
app.register_blueprint(users_bp)  

@app.route('/')
def home():
   return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)


