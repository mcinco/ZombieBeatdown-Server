# Created by: Micah Cinco
# Version 1. October 2014

import mongo, task, json, pprint, os, pymongo, sys
from datetime import datetime
from os import curdir, sep
from pymongo import MongoClient

MONGO_URL = 'mongodb://admin:ENGR489zb@kahana.mongohq.com:10046/ZombieBeatdown'

def refresh_tasks():
    """Reset all tasks in the database to progress state == "idle"."""  
    client = MongoClient(MONGO_URL)
    db = client.ZombieBeatdown
    collection = db.evaluation
    
    for task in collection.find():
        collection.update(({ "progress": "completed" }) , {'$set':{'progress': "idle", 'tid_list': []}}, upsert=False, multi=False)
    return 'Successfully refreshed all tasks to idle.'

if __name__ == '__main__':
    print refresh_tasks()
