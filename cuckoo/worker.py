from bson import json_util
import json, time
import mongo, task, taskhandler, cuckoo


tid_list=[]

def start_worker():
    task = mongo.pull_task()
    if task != None:
        #print json.dumps(task, sort_keys=True, indent=4, default=json_util.default)
        #print task['_id']
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
            print tid_list
            #mongo.get_tasklist(_id)
#             for tid in tasklist:
#             taskhandler.check_task('1')
            #print 'about to check db'
    except KeyboardInterrupt:
        return

if __name__ == '__main__':
    _id = start_worker()
    
    if _id == None:
        print "No tasks in 'idle' state to pull"
        
    else:
        check_status(_id)