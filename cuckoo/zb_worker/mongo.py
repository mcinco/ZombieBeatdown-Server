# Created by: Micah Cinco
# Version 1. October 2014

import pymongo, json, worker, taskhandler
from pymongo import MongoClient
from bson.json_util import dumps

MONGO_URL = 'mongodb://admin:ENGR489zb@kahana.mongohq.com:10046/ZombieBeatdown'

client = MongoClient(MONGO_URL)
db = client.ZombieBeatdown
collection = db.tasks

def pull_task():    
    """Pulls task from MongoHQ DB according to priority and must be in "idle" state.
    @return task"""
            
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
    """Update tasklist of given task."""    
    collection.update({ "_id": task['_id']} , {'$set':{'tid_list': tasklist}})
    
def task_done(_id):   
    """Change given task's progress to "completed".""" 
    for t in collection.find({ "_id": _id }):
        collection.update(t , {'$set':{'progress': "completed"}}, upsert=False, multi=False)