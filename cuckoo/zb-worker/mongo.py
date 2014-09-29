import pymongo, json
from pymongo import MongoClient
from bson.json_util import dumps

MONGO_URL = 'mongodb://admin:ENGR489zb@kahana.mongohq.com:10046/ZombieBeatdown'

def pull_task():  
    client = MongoClient(MONGO_URL)
    db = client.ZombieBeatdown
    collection = db.tasks
          
    if collection.find_one({ "progress":"idle" }) == None:
        return None
        
    else:
        if collection.find_one({ "progress":"idle", "priority":"High" }) == None:
            if collection.find_one({ "progress":"idle", "priority":"Normal" }) == None:
                for task in collection.find({ "progress":"idle", "priority":"Low" }):
                    collection.update(task , {'$set':{'progress': "inprogress"}}, upsert=False, multi=False)
                    return task
            
            else:
                for task in collection.find({ "progress":"idle", "priority":"Normal" }):
                    collection.update(task , {'$set':{'progress': "inprogress"}}, upsert=False, multi=False) 
                    return task
            
        else: 
            for task in collection.find({ "progress":"idle", "priority":"High" }):
                collection.update(task , {'$set':{'progress': "inprogress"}}, upsert=False, multi=False)
                return task              