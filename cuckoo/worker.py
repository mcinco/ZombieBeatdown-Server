from bson import json_util
import os, random, sys, json

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))

from lib.cuckoo.common.colors import bold, green, red, yellow
from lib.cuckoo.core.database import Database
import zb_worker.mongo
import cuckoo

tasklist=[]

def start_worker():
    task = mongo.pull_task()
    if task != None:
        #print json.dumps(task, sort_keys=True, indent=4, default=json_util.default)
        print task['_id']
        tasklist = taskhandler.add_urls(task)
#         while True:
#             taskhandler.check_status(task)
    else:
        print "No tasks in 'idle' state to pull"

if __name__ == '__main__':
    start_worker()
    cuckoo.main()