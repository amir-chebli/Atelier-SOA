# app.py
from flask import Flask, jsonify, request, render_template
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# Sample data for the RESTful API
resources = [{'id': 1, 'name': 'Resource 1'}, {'id': 2, 'name': 'Resource 2'}]

# Read user credentials from the text file
def read_user_credentials():
    users = {}
    with open('C:/Users/chebl/Desktop/Files/Studies/SOA/Atelier 4/users.txt', 'r') as file:
        for line in file:
            username, password = line.strip().split(',')
            users[username] = password
    return users

# Verify password callback for HTTPBasicAuth
@auth.verify_password
def verify_password(username, password):
    # Retrieve user credentials from the file
    users = read_user_credentials()
    return users.get(username) == password

# Route to retrieve all resources
@app.route("/", methods=['GET'])
@auth.login_required  # Enforce authentication for the root route
def get_all_resources():
    return jsonify(resources)

# Route to retrieve a specific resource by ID
@app.route("/<int:resource_id>", methods=['GET'])
def get_resource(resource_id):
    resource = next((r for r in resources if r['id'] == resource_id), None)
    if resource:
        return jsonify(resource)
    else:
        return jsonify({'error': 'Resource not found'}), 404

# Login route
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if auth.verify_password(username, password):
            return render_template('home.html', username=username)
        else:
            return render_template('login.html', message='Invalid credentials')

    return render_template('login.html', message='')

# Secure route that requires authentication
@app.route("/secure-resource", methods=['GET'])
@auth.login_required
def get_secure_resource():
    return jsonify({'message': 'Authenticated access to secure resource'})

# ... (other routes and CRUD operations)

if __name__ == "__main__":
    app.run(debug=True)
