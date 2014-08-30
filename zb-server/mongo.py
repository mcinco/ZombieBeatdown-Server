import pymongo, json
from pymongo import MongoClient

MONGO_URL = 'mongodb://admin:ENGR489zb@kahana.mongohq.com:10046/ZombieBeatdown'
#task = ""

def push_task(doc):
    task = doc    
    client = MongoClient(MONGO_URL)
    db = client.ZombieBeatdown
    collection = db.tasks
    collection.insert(task.__dict__)
    
#     for t in collection.find():
#         print t

    

