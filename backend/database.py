from pymongo import MongoClient, ReturnDocument
def get_database():
   
   CONNECTION_STRING = "mongodb://localhost:27017/devopsdb"
   client = MongoClient(CONNECTION_STRING)
   return client['database']

dbname = get_database()
collection = dbname['employees']

def get_new_id(collection_name):
   document = collection.find_one_and_update(
      {'collection_name': collection_name},
      {'$inc': {'sequence_value': 1}},
      return_document=ReturnDocument.AFTER,
      upsert=True
   )
   return document['sequence_value']

