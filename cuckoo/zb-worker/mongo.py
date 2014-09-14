
import pymongo, json, pprint
from pymongo import MongoClient

MONGO_URL = 'mongodb://admin:ENGR489zb@kahana.mongohq.com:10046/ZombieBeatdown'

def pull_task():  
    client = MongoClient(MONGO_URL)
    db = client.ZombieBeatdown
    collection = db.tasks
    list = []
    id = ""
           
    if collection.find_one({ "progress":"idle" }) == None:
        return "No tasks in 'idle' state to pull"
        
    else:
        if collection.find_one({ "progress":"idle", "priority":"High" }) == None:
            if collection.find_one({ "progress":"idle", "priority":"Normal" }) == None:
                task = collection.find({ "progress":"idle", "priority":"Low" })
                for key in task:
                    id = key['_id']
                collection.update({ "_id": id } , {'$set':{'progress': "inprogress"}}, upsert=False, multi=False)  
            
            else:
                task = collection.find({ "progress":"idle", "priority":"Normal" })
                for key in task:
                    id = key['_id']
                collection.update({ "_id": id } , {'$set':{'progress': "inprogress"}}, upsert=False, multi=False)  
                
        else: 
            task = collection.find({ "progress":"idle", "priority":"High" })
            for key in task:
                id = key['_id']
            collection.update({ "_id": id } , {'$set':{'progress': "inprogress"}}, upsert=False, multi=False)         
                      