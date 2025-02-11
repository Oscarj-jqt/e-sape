from flask import Flask
from routes.auth import auth_bp  
from routes.users import users_bp

app = Flask(__name__)

# Configuration de la clé JWT
app.config['JWT_SECRET_KEY'] = 'web2'

# Enregistrement des Blueprints
app.register_blueprint(auth_bp) 
app.register_blueprint(users_bp)  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
