import mongo, task, json, pprint, os, pymongo, sys
from os import curdir, sep
from pymongo import MongoClient

MONGO_URL = 'mongodb://admin:ENGR489zb@kahana.mongohq.com:10046/ZombieBeatdown'

def refresh_tasks(progress):  
    client = MongoClient(MONGO_URL)
    db = client.ZombieBeatdown
    collection = db.tasks
    
    for task in collection.find():
        collection.update(({ "progress": "inprogress" } or { "progress": "completed" }) , {'$set':{'progress': "idle"}}, upsert=False, multi=False)
    return 'Successfully changed all tasks to idle.'

if __name__ == '__main__':
    prog = sys.argv
    print refresh_tasks(prog)