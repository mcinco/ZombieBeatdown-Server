import mongo, task, json, minionrun
from bson import json_util

if __name__ == '__main__':
    task = mongo.pull_task()
    if task != None:
        print json.dumps(task, sort_keys=True, indent=4, default=json_util.default)
        print task['_id']
        #minionrun.run_scripts(task)
    else:
        print "No tasks in 'idle' state to pull"