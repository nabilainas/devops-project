from flask import Flask,request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

def get_database():
    CONNECTION_STRING = "mongodb://nabil:ainas@mongo:27017/"
    client = MongoClient(CONNECTION_STRING)
    return client['database']

dbname = get_database()
collection = dbname['employees']

app = Flask(__name__)
CORS(app)

@app.route("/api/v1/employees", methods=['GET','POST'])
def employees():
    cursor = collection.find({}, {"_id":0})
    list = [i for i in cursor]
    if request.method == 'GET':
        return jsonify(list), 200
    
    if request.method == 'POST':
        data = request.get_json()
        data["id"] = len(list) + 1
        collection.insert_one(data)
        return jsonify(data), 200


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

