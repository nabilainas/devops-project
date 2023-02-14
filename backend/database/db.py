from pymongo import MongoClient
def get_database():
   
   CONNECTION_STRING = "mongodb://localhost:27017/devopsdb"
   client = MongoClient(CONNECTION_STRING)
   return client['database']

dbname = get_database()

def new_employee(username):
   item = {
      "Name" : username,
      "max_discount" : "10%",
      "batch_number" : "RR450020FRG",
      "price" : 340,
      "category" : "kitchen appliance"
   }

   collection = dbname['employee']
   collection.insert_one(item)

   return "done"

def get_employee(username):
   collection = dbname['employee']
   return collection.find_one({"Name" : username})