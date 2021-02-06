from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import Flask, jsonify, request

from db import user_collection
from nlp import tokenize, pos_tag, rm_stop_words, bag_of_words

app = Flask(__name__)


@app.route('/process_text', methods=['POST'])
def process_text():
    _json = request.get_json(force=True)
    if not "method" in _json or not "text" in _json:
        return not_found()
    text = _json['text']
    method = _json['method']
    result = None

    if method == "tokenization":
        result = tokenize(text)
    elif method == "pos_tag":
        result = pos_tag(tokenize(text))
    elif method == "rm_stop_words":
        result = rm_stop_words(text)
    elif method == "bag_of_words":  # expecting an array of texts
        result = bag_of_words(text)
    return jsonify({"success": True, "data": result})


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
        resp = jsonify('Data added successfully!')
        resp.status_code = 200
        return resp
    else:
        return not_found()


@app.route('/data/<id>', methods=['DELETE'])
def delete_user(id):
    user_collection.delete_one({'_id': ObjectId(id)})
    resp = jsonify('Data deleted successfully!')
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
