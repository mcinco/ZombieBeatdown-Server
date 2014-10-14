# Created by: Micah Cinco
# Version 1. October 2014

from bson import json_util
import json, time
import mongo, task, taskhandler, cuckoo
from lib.cuckoo.common.colors import bold, green, red, yellow
tid_list=[]

def start_worker():
    """Pull a task from MongoHQ DB and 
    add URLs for processing queue in Cuckoo db.
    @return task_id"""
    
    task = mongo.pull_task()
    if task != None:
        global tid_list 
        tid_list = taskhandler.add_urls(task)
#        print tid_list
        return task['_id']
    else:
        return None
        
def check_status(_id):
    """Periodically check whether all URL analysis is finished."""
    try:
        while True:
            time.sleep(5)
            task_status = taskhandler.task_done(tid_list)

            if task_status == False:
                print(bold(yellow("Task Not Done")) + ": still processing URLs")
            if task_status == True:
                print (bold(green("Task Completed"))+ ": All URLs done have been analyzed")
                mongo.task_done(_id)
                break
    except KeyboardInterrupt:
        return

if __name__ == '__main__':
    _id = start_worker()
    
    if _id == None:
        print(bold(red("Error")) + ": no tasks in 'idle' state to pull") 
    else:
        check_status(_id)