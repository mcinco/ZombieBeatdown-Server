# Created by: Micah Cinco
# Version 1. October 2014

import pymongo, json, pprint
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.errors import InvalidId

MONGO_URL = 'mongodb://admin:ENGR489zb@kahana.mongohq.com:10046/ZombieBeatdown'

"""Pushes task to MongoHQ DB.
    @return: ObjectId"""
def push_task(task):    
    client = MongoClient(MONGO_URL)
    db = client.ZombieBeatdown
    collection = db.evaluation
    return collection.insert(task.__dict__)
    
"""Pulls all tasks from MongoHQ DB with matching progress states.
    @return: list_of_tasks"""
def check_tasks(progress):
    client = MongoClient(MONGO_URL)
    db = client.ZombieBeatdown
    collection = db.evaluation
    list = []
    for task in collection.find({ "progress":progress }):
        list.append(task)
    return list

"""Deletes all tasks with a matching progress state.
	@return list_of_deleted_tasks"""
def delete_progress(progress):   
    client = MongoClient(MONGO_URL)
    db = client.ZombieBeatdown
    collection = db.evaluation
    list = []
    for task in collection.find({ "progress":progress }):
        list.append(task['_id'])
        collection.remove(task)
    return list
    
"""Deletes task with matching ObjectId."""
def delete_task(taskid):   
    client = MongoClient(MONGO_URL)
    db = client.ZombieBeatdown
    collection = db.evaluation
    try:
        task = collection.find_one({ "_id":ObjectId(taskid) })
        if task == None:
            return "<h1>Task ID entered is not found.\n</h1>"
        else: 
            collection.remove(task)
            return "<h1>Task successfully deleted.\n</h1>"
    except InvalidId:
        return "<h1>Task ID entered is not valid.\n</h1>"

"""Return the total number of tasks with a matching progress."""
def print_size(progress):
    prog = progress 
    client = MongoClient(MONGO_URL)
    db = client.ZombieBeatdown
    collection = db.evaluation
    return "\nThere are %d tasks in the database and %d are in \"%s\" status." % (collection.count(), collection.find({ "progress":prog }).count(), prog)

"""Return the total number of tasks with a matching progress."""
def get_progress_size(progress):
    client = MongoClient(MONGO_URL)
    db = client.ZombieBeatdown
    collection = db.evaluation
    return collection.find({ "progress":progress }).count()