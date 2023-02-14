# Get the database using the method we defined in pymongo_test_insert file
from database.db import get_database
dbname = get_database()

collection_name = dbname["employee"]

item_1 = {
  "item_name" : "Nabil",
}

item_2 = {
  "item_name" : "AINAS",
}

collection_name.insert_many([item_1,item_2])