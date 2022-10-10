from pymongo import MongoClient
from pprint import pprint

client = pymongo.MongoClient("mongodb://localhost:27017/")
db=client.admin
for db in client.list_databases():
    print(db)