from os import name
from flask import Flask, render_template, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity


app = Flask(__name__)

# Jwt key configuration 
app.config['JWT_SECRET_KEY'] = 'web2'
jwt = JWTManager(app)


# Liste de livres
books = [
    {"id": 1, "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "year": 1997},
    {"id": 2, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"id": 3, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 4, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 5, "title": "A Promised Land", "author": "Barack Obama", "year": 2020}
]

@app.route('/')
def home():
   return render_template('index.html')


@app.route('/signup')
def index():
   return render_template('signup.html')

# To create automatically a JWT token 
# The login method has a jwt authentication 
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

# Protect a route with jwt_required
# secured route to get sure we are logged
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


if __name__ == "__main__":
    app.run()

@app.route('/add')
def add():
   return render_template('add.html')

@app.route('/search', methods=['GET'])
def search():

    exist = False
    film = {}
    query = request.args.get('query')

    for book in books:
        if book['author'] == query:
            exist = True
            film = book
            break

    if exist:
        return film
    else:
        return "No book found"


@app.route('/ajout', methods=['POST'])
def add_book():

    title = request.form['titre']
    author = request.form['auteur']
    year = request.form['annee']

    id = len(books) + 1

    new_book = {"id": id, "title": title, "author": author, "year": year}
    books.append(new_book)

    return books

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
