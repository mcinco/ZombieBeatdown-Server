import mongo, task, json, taskhandler
from bson import json_util

tasklist=[]

if __name__ == '__main__':
    task = mongo.pull_task()
    if task != None:
        #print json.dumps(task, sort_keys=True, indent=4, default=json_util.default)
        print task['_id']
        tasklist = taskhandler.add_urls(task)
#         while True:
#             taskhandler.check_status(task)
    else:
        print "No tasks in 'idle' state to pull"