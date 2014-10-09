from bson import json_util
import json, time
import mongo, task, taskhandler, cuckoo


tid_list=[]

def start_worker():
    task = mongo.pull_task()
    if task != None:
        global tid_list 
        tid_list = taskhandler.add_urls(task)
        print tid_list
        return task['_id']
    else:
        return None
        
def check_status(_id):
    try:
        while True:
            time.sleep(5)
            task_status = taskhandler.task_done(tid_list)

            if task_status == False:
                print 'Task not done\n'
            if task_status == True:
                print 'All URLs done - Task is completed!\n'
                mongo.task_done(_id)
                break
    except KeyboardInterrupt:
        return

if __name__ == '__main__':
    _id = start_worker()
    
    if _id == None:
        print "No tasks in 'idle' state to pull"
        
    else:
        check_status(_id)