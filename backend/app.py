from flask import Flask,request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)
client = MongoClient("mongodb://nabil:ainas@mongo:27017/")
dbname = client['database']
collection = dbname['employees']

@app.route("/api/v1/employees", methods=['GET','POST'])
def employees():
    if request.method == 'GET':
        return jsonify([i for i in collection.find({}, {"_id":0})]), 200
    if request.method == 'POST':
        data = request.get_json()
        data["id"] = len([i for i in collection.find({}, {"_id":0})]) + 1
        collection.insert_one(data)
        return jsonify(data), 200

@app.route("/api/v1/employees/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def manage(id):
    if request.method == 'GET':
        return [element for element in [i for i in collection.find({}, {"_id":0})] if element["id"] == id][0]
    if request.method == 'PUT':
        result = collection.update_one({"id": int(id)}, {"$set": request.get_json()})
        return jsonify({"result": "Employee updated"}) if result.modified_count == 1 else jsonify({"error": "Employee not found"}) 
    if request.method == 'DELETE':
        result = collection.delete_one({'id': int(id)})
        return jsonify({'result': 'Employee deleted'}) if result.deleted_count == 1 else jsonify({'error': 'Employee not found'})