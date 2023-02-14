from flask import Flask,request, jsonify
from bson.objectid import ObjectId
from database import *

app = Flask(__name__)

@app.route("/employees/", methods=['GET'])
def get_all_elements():
    elements = collection.find()
    result = []

    for element in elements:
        element["_id"] = str(element["_id"])
        result.append(element)

    return jsonify(result)

@app.route("/employees/<username>", methods=['POST'])
def new_user(username):
    item = {
        "Name" : username,
    }
    collection.insert_one(item)

    return "ok"


@app.route('/employees/<string:id>/<new_username>', methods=['GET','PUT', 'DELETE'])
def update_element(id, new_username):
    data = {
        "Name" : new_username
    }
    result = collection.update_one({"_id": ObjectId(id)}, {"$set": data})

    if result.modified_count == 1:
        element = collection.find_one({"_id": ObjectId(id)})
        element["_id"] = str(element["_id"])
        return jsonify({"result": element}), 200
    else:
        return jsonify({"error": "Element not found"}), 404

@app.route('/employees/<string:id>', methods=['GET','PUT','DELETE'])
def delete_document(id):
    result = collection.delete_one({'_id': ObjectId(id)})

    if result.deleted_count == 1:
        return jsonify({'result': 'Document deleted'}), 200
    else:
        return jsonify({'error': 'Document not found'}), 404
