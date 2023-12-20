# app.py (with CRUD operations and HTML templates)
from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__)

resources = [{'id': 1, 'name': 'Resource 1'}, {'id': 2, 'name': 'Resource 2'}]

@app.route("/resources", methods=['GET'])
def get_all_resources():
    return render_template('index.html', resources=resources)

@app.route("/resources/new", methods=['GET', 'POST'])
def create_new_resource():
    if request.method == 'POST':
        new_resource = {'id': len(resources) + 1, 'name': request.form.get('name')}
        resources.append(new_resource)
        return redirect(url_for('get_all_resources'))
    return render_template('create.html')

@app.route("/resources/<int:resource_id>", methods=['GET'])
def get_resource(resource_id):
    resource = next((r for r in resources if r['id'] == resource_id), None)
    if resource:
        return render_template('detail.html', resource=resource)
    else:
        return jsonify({'error': 'Resource not found'}), 404

@app.route("/resources/<int:resource_id>/edit", methods=['GET', 'POST'])
def edit_resource(resource_id):
    resource = next((r for r in resources if r['id'] == resource_id), None)
    if request.method == 'POST':
        if resource:
            resource['name'] = request.form.get('name', resource['name'])
            return redirect(url_for('get_all_resources'))
    if resource:
        return render_template('update.html', resource=resource)
    else:
        return jsonify({'error': 'Resource not found'}), 404

@app.route("/resources/<int:resource_id>/delete", methods=['POST'])
def delete_resource(resource_id):
    global resources
    resources = [r for r in resources if r['id'] != resource_id]
    return redirect(url_for('get_all_resources'))

if __name__ == "__main__":
    app.run(debug=True)
