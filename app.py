from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from routes.auth import auth_bp
from routes.users import users_bp, blacklisted_tokens
from datetime import timedelta
from flask_cors import CORS
from flask_graphql import GraphQLView
#from database.graph import schema 

app = Flask(__name__)
CORS(app)  # Liaison Flask avec React

# API GraphQL
app.add_url_rule("/graphql", view_func=GraphQLView.as_view(
   "graphql",
 #  schema=schema,
   graphiql=True  # Interface GraphiQL activée
))

# Configuration JWT
app.config['JWT_SECRET_KEY'] = 'web2'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
jwt = JWTManager(app)

# Vérifier si un token est blacklisté
@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):
    return jwt_payload["sub"] in blacklisted_tokens  # Vérifie si l'utilisateur est dans la liste noire

# Enregistrement des Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(users_bp)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
