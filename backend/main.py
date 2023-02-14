from flask import Flask,request, jsonify
from bson.objectid import ObjectId
from database import *

app = Flask(__name__)

@app.route("/api/v1/employees", methods=['GET'])
def get_all_elements():
    elements = collection.find()
    result = []

    for element in elements:
        element["_id"] = str(element["_id"])
        result.append(element)

    return jsonify(result)

@app.route("/api/v1/employees/<username>", methods=['GET','POST'])
def new_user(username):
    item = {
        "Name" : username,
    }
    collection.insert_one(item)

    return "ok"


# @app.route('/api/v1/employees/<string:id>', methods=['GET','PUT', 'DELETE'])
# def update_element(id):
#     result = collection.update_one({"_id": ObjectId(id)}, {"$set": data})

#     if result.modified_count == 1:
#         element = collection.find_one({"_id": ObjectId(id)})
#         element["_id"] = str(element["_id"])
#         return jsonify({"result": element}), 200
#     else:
#         return jsonify({"error": "Element not found"}), 404

# @app.route('/employees/<string:id>', methods=['GET','PUT','DELETE'])
# def delete_document(id):
#     result = collection.delete_one({'_id': ObjectId(id)})

#     if result.deleted_count == 1:
#         return jsonify({'result': 'Document deleted'}), 200
#     else:
#         return jsonify({'error': 'Document not found'}), 404

