from pymongo import MongoClient
from pprint import pprint

MONGO_URL = "mongodb://mongo:27017"
client = MongoClient(MONGO_URL)
db = client.records
col = db.links
col.insert_one({"link":"Lawrence.org"})
links.col.find({})
for link in links:
    pprint(link)