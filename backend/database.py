from pymongo import MongoClient
def get_database():
   
   CONNECTION_STRING = "mongodb://localhost:27017/devopsdb"
   client = MongoClient(CONNECTION_STRING)
   return client['database']

dbname = get_database()
collection = dbname['employees']


