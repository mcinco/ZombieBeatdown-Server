import task, json
from bson import json_util
#from cuckoo.utils import submit

urllist = []

def run_scripts(task):  
    for url in task['urls']:
        print 'hello'        