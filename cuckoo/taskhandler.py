#!/usr/bin/env python
# Copyright (C) 2010-2014 Cuckoo Sandbox Developers.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.
# Edited by Micah Cinco

import task, json, mongo
import os, random, sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))

from lib.cuckoo.common.colors import bold, green, red, yellow
from lib.cuckoo.core.database import Database

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
            
def check_task(tid):
    db = Database()
    
    completedlist = db.list_tasks(offset=offset, status=TASK_COMPLETED)
    completedlist += db.list_tasks(offset=offset, status=TASK_REPORTED)
    print completedlist
        
        
if __name__ == '__main__':
    delete_all()