from flask import Flask, jsonify, request
from db import db, user_collection, client
from bson.objectid import ObjectId
from bson.json_util import dumps
import json

app = Flask(__name__)


@app.route('/data', methods=['GET'])
def get_all_data():
    data = user_collection.find()
    resp = dumps(data)
    return resp

@app.route('/data/<id>', methods=['GET'])
def get_data(id):
    data = user_collection.find_one({'_id': ObjectId(id)})
    resp = dumps(data)
    return resp


@app.route('/data', methods=['POST'])
def save_new_data():
    _json = request.get_json(force=True)
    print(_json)
    _name = _json['name']
    if _name and request.method == 'POST':
        user_collection.insert_one({"name": _name})
        resp = jsonify('User added successfully!')
        resp.status_code = 200
        return resp
    else:
        return not_found()


@app.route('/data/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.user.delete_one({'_id': ObjectId(id)})
    resp = jsonify('User deleted successfully!')
    resp.status_code = 200
    return resp


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == '__main__':
    app.run(port=8000)
