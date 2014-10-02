import pymongo, json, worker, taskhandler
from pymongo import MongoClient
from bson.json_util import dumps

MONGO_URL = 'mongodb://admin:ENGR489zb@kahana.mongohq.com:10046/ZombieBeatdown'

client = MongoClient(MONGO_URL)
db = client.ZombieBeatdown
collection = db.tasks

def pull_task():    
            
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
            
def update_tasklist(task, tasklist):    
    collection.update({ "_id": task['_id']} , {'$set':{'tid_list': tasklist}})
    
def get_tasklist(_id):    
    for t in collection.find({ "_id": _id }):
        task = t
    return task['tid_list']   