from pymongo import MongoClient
from pprint import pprint

MONGO_URL = "mongodb://27017"
client = MongoClient(MONGO_URL)
db=client.admin
db_list = db.command("listDatabases")
pprint(db_list)