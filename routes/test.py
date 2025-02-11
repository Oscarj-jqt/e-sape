from os import name
from flask import Flask, render_template, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity



app = Flask(__name__)

# Jwt key configuration 
app.config['JWT_SECRET_KEY'] = 'web2'
jwt = JWTManager(app)


# Liste des users
users = [
    {"id": 1, "username": "admin", "password": "123"}
]

@app.route('/')
def home():
   return render_template('index.html')


@app.route('/signup')
def signup():
   return render_template('signup.html')

@app.route('/login')
def login():
   return render_template('login.html')

# To create automatically a JWT token 
# The login method has a jwt authentication 
@app.route("/login", methods=["POST"])
def check_login():
    # Log with username and password
    username = request.form.get('username')
    password = request.form.get('password')

    for user in users:
        if user['username'] == username and user['password'] == password:
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({"msg": "Bad username or password"}), 401

    # username = request.json.get("username", None)
    # password = request.json.get("password", None)
    # if username != "test" or password != "test":
    #     return jsonify({"msg": "Bad username or password"}), 401

    # access_token = create_access_token(identity=username)
    # return jsonify(access_token=access_token)


# Home page after the JWT auth
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

# add user to database
@app.route('/adduser', methods=['POST'])
def adduser():
    username = request.form.get("username")
    password = request.form.get("password")
    email = request.form.get("email")

    # Vérifier si l'utilisateur existe déjà
    for user in users:
        if user["username"] == username:
            return jsonify({"msg": "Username already taken"}), 400

    # hashed_password = generate_password_hash(password)

    new_user = {
        "id": len(users) + 1,
        "username": username,
        "password": password,
        "email": email
    }
    users.append(new_user)

    return jsonify({"msg": "User added successfully"}), 201



@app.route('/add')
def add():
   return render_template('add.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

