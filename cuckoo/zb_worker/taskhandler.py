#!/usr/bin/env python
# Copyright (C) 2010-2014 Cuckoo Sandbox Developers.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.
# Edited by Micah Cinco

import task, json, mongo
import os, random, sys
from pprint import pprint
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))

from lib.cuckoo.common.colors import bold, green, red, yellow
from lib.cuckoo.core.database import Database, TASK_PENDING, TASK_RUNNING, Task
from lib.cuckoo.core.database import TASK_COMPLETED, TASK_RECOVERED
from lib.cuckoo.core.database import TASK_REPORTED, TASK_FAILED_ANALYSIS
from lib.cuckoo.core.database import TASK_FAILED_PROCESSING

tasklist = []

def add_urls(task):  
    for url in task['urls']:
        db = Database()

        task_id = db.add_url(url,
                     timeout=task['timeout'],
                     priority=task['priority'])

        if task_id:
            tasklist.append(task_id)
            print(bold(green("Success")) + u": URL \"{0}\" added as task with ID {1}".format(url, task_id))
        else:
            print(bold(red("Error")) + ": adding task to database") 
    
    mongo.update_tasklist(task, tasklist)
    return tasklist
    
def delete_all():  
    db = Database()
    list = db.list_tasks()
    
    if not list:
        print 'No tasks to be deleted'
    else: 
        for url in list:
            db.delete_task(db.count_tasks())
            print url
            
def task_done(tid_list):
    db = Database()

    tasks_count = db.count_tasks(status=TASK_COMPLETED, tid_list=tid_list)
    tasks_count += db.count_tasks(status=TASK_REPORTED, tid_list=tid_list)
    print tasks_count
    
    if tasks_count < len(tid_list):
        return False
    elif tasks_count == len(tid_list):
        return True
        
        
if __name__ == '__main__':
    delete_all()
