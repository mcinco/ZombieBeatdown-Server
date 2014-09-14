import pymongo, json, pprint
from pymongo import MongoClient

MONGO_URL = 'mongodb://admin:ENGR489zb@kahana.mongohq.com:10046/ZombieBeatdown'

def push_task(doc):
    task = doc    
    client = MongoClient(MONGO_URL)
    db = client.ZombieBeatdown
    collection = db.tasks
    return collection.insert(task.__dict__)
    
def check_tasks(progress):
    prog = progress    
    client = MongoClient(MONGO_URL)
    db = client.ZombieBeatdown
    collection = db.tasks
    list = []
    for task in collection.find({ "progress":prog }):
        list.append(task)
    return list
    
def print_size(progress):
    prog = progress 
    client = MongoClient(MONGO_URL)
    db = client.ZombieBeatdown
    collection = db.tasks
    return "\nThere are %d tasks in the database and %d are in \"%s\" status." % (collection.count(), collection.find({ "progress":prog }).count(), prog)