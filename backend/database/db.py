from pymongo import MongoClient
def get_database():
   
   CONNECTION_STRING = "mongodb://localhost:27017/devopsdb"
   client = MongoClient(CONNECTION_STRING)
   return client['database']

dbname = get_database()
collection = dbname['employee']

def new_employee(username):
   item = {
      "Name" : username,
   }

   collection.insert_one(item)

   return "done"

