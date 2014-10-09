import pymongo, json, pprint
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.errors import InvalidId

MONGO_URL = 'mongodb://admin:ENGR489zb@kahana.mongohq.com:10046/ZombieBeatdown'

def push_task(task):    
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

def delete_progress(progress):   
    client = MongoClient(MONGO_URL)
    db = client.ZombieBeatdown
    collection = db.tasks
    list = []
    for task in collection.find({ "progress":progress }):
        list.append(task['_id'])
        collection.remove(task)
    return list
    
def delete_task(taskid):   
    client = MongoClient(MONGO_URL)
    db = client.ZombieBeatdown
    collection = db.tasks
    try:
        task = collection.find_one({ "_id":ObjectId(taskid) })
        if task == None:
            return "<h1>Task ID entered is not found.\n</h1>"
        else: 
            collection.remove(task)
            return "<h1>Task successfully deleted.\n</h1>"
    except InvalidId:
        return "<h1>Task ID entered is not valid.\n</h1>"
    
#     return list

def print_size(progress):
    prog = progress 
    client = MongoClient(MONGO_URL)
    db = client.ZombieBeatdown
    collection = db.tasks
    return "\nThere are %d tasks in the database and %d are in \"%s\" status." % (collection.count(), self.get_progress_size(prog), prog)

def get_progress_size(progress):
    client = MongoClient(MONGO_URL)
    db = client.ZombieBeatdown
    collection = db.tasks
    return collection.find({ "progress":progress }).count()