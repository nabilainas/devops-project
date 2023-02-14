from flask import Flask,request, jsonify
from bson.objectid import ObjectId
from flask_cors import CORS
from database import *

app = Flask(__name__)
CORS(app)

@app.route("/api/v1/employees", methods=['GET'])
def get_all_elements():
    elements = collection.find({'_id': {'$nin': [ObjectId('63ec18ec483297cdde99e306'),  ObjectId('63ec18ecfe31bf1a0ac7a8d3') ]}})
    result = []

    for element in elements:
        element["_id"] = str(element["_id"])
        result.append(element)

    return jsonify(result)

@app.route("/api/v1/employees", methods=['GET','POST'])
def new_user():
    item = request.get_json()
    item["id"] = get_new_id('id_incrementation')
    collection.insert_one(item)
    item["_id"] = str(item["_id"])
    
    

    return item


@app.route('/api/v1/employees/<int:id>', methods=['GET','PUT'])
def update_element(id):
    item = request.get_json()
    result = collection.update_one({"id": int(id)}, {"$set": item})

    if result.modified_count == 1:
        element = collection.find_one({"id": int(id)})
        element["_id"] = str(element["_id"])
        return jsonify({"result": element}), 200
    else:
        return jsonify({"error": "Element not found"}), 404, item

@app.route('/api/v1/employees/<int:id>', methods=['GET','DELETE'])
def delete_document(id):
    result = collection.delete_one({'id': int(id)})

    if result.deleted_count == 1:
        return jsonify({'result': 'Document deleted'}), 200
    else:
        return jsonify({'error': 'Document not found'}), 404

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)