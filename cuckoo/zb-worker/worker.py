import mongo, task, json, pprint, os
from os import curdir, sep
from bson.json_util import dumps

if __name__ == '__main__':
    task = mongo.pull_task()
    print task
    