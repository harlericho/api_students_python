from flask import Flask, app, jsonify, request
from flask_cors import CORS
from flask_mysqldb import MySQL


# connection mysql
from config.db import get_connection
# models
import models.students

# config app
app=Flask(__name__)
CORS(app)
mysql = MySQL(get_connection(app))

# routers
@app.route('/')
def index():
    try:
        data = models.students.list(mysql)
        list = []
        for i in data:
            file = {'id': i[0], 'names': i[1], 'email': i[2],
                'age': i[3]}
            list.append(file)
        return jsonify({'students': list})
    except Exception as e:
        return jsonify(e)

@app.route('/<int:id>', methods=['GET'])
def search(id):
    try:
        data = models.students.listId(mysql,id)
        if data != None:
            file = {'id': data[0], 'names': data[1], 'email': data[2],
                'age': data[3]}
            return jsonify({'students': file})
        else:
            return jsonify({'message': 'No data with that id'})
    except Exception as e:
        return jsonify(e)

@app.route('/', methods=['POST'])
def save():
    try:
        json = request.json
        if request.method == 'POST':
            names = json.get('names')
            email = json.get('email')
            age = json.get('age')
        models.students.post(mysql,names,email,age)
        return jsonify({'message': 'Saved data'})
    except Exception as e:
        return jsonify(e)

@app.route('/<int:id>', methods=['PUT'])
def update(id):
    try:
        json = request.json
        if request.method == 'PUT':
            names = json.get('names')
            email = json.get('email')
            age = json.get('age')
        models.students.put(mysql,names,email,age,id)
        return jsonify({'message': 'Updated data'})
    except Exception as e:
        return jsonify(e)

@app.route('/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        file = models.students.listId(mysql,id)
        if file != None:
            models.students.delete(mysql,id)
            return jsonify({'students': 'Deleted data'})
        else:
            return jsonify({'message': 'No data with that id'})
    except Exception as e:
        return jsonify(e)


# start server
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
