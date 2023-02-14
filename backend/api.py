from flask import Flask, jsonify
from bson.objectid import ObjectId
import database.db as db

app = Flask(__name__)

@app.route("/post/<username>")
def new_user(username):
    item = {
        "Name" : username,
    }
    db.collection.insert_one(item)

    return db.new_employee(username)

@app.route("/get/all")
def get_all_elements():
    elements = db.collection.find()
    result = []

    for element in elements:
        element["_id"] = str(element["_id"])
        result.append(element)

    return jsonify(result)


@app.route("/get/<string:id>", methods=['GET'])
def get_element(id):
    object_id = ObjectId(id)
    element = db.collection.find_one({"_id": object_id })
    if element:
        element["_id"] = str(element["_id"])
        return jsonify({"result": element})
    else:
        return jsonify({"error": "Element not found"}), 404


@app.route('/update/<string:id>/<new_username>', methods=['GET','PUT', 'DELETE'])
def update_element(id, new_username):
    data = {
        "Name" : new_username
    }
    result = db.collection.update_one({"_id": ObjectId(id)}, {"$set": data})

    if result.modified_count == 1:
        element = db.collection.find_one({"_id": ObjectId(id)})
        element["_id"] = str(element["_id"])
        return jsonify({"result": element}), 200
    else:
        return jsonify({"error": "Element not found"}), 404

@app.route('/delete/<string:id>', methods=['GET','PUT','DELETE'])
def delete_document(id):
    result = db.collection.delete_one({'_id': ObjectId(id)})

    if result.deleted_count == 1:
        return jsonify({'result': 'Document deleted'}), 200
    else:
        return jsonify({'error': 'Document not found'}), 404
