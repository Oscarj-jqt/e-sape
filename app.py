from flask import Flask
from flask import Flask, render_template, request, jsonify
from flask_jwt_extended import JWTManager
from routes.auth import auth_bp 
from routes.users import users_bp
from datetime import timedelta


app = Flask(__name__)


# Configuration de la clé JWT
app.config['JWT_SECRET_KEY'] = 'e-sape'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)  
jwt = JWTManager(app)

# Enregistrement des Blueprints
app.register_blueprint(auth_bp) 
app.register_blueprint(users_bp)  

@app.route('/')
def home():
   return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
