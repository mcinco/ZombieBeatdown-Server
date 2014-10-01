import json
from datetime import datetime

class Task(object):
    urls = []
    priority = ""
    timeout = 100
    tid_list = []

    # The class "constructor" 
    def __init__(self, urls, timeout, priority):
        self.urls = urls
        self.priority = priority
        self.timeout = timeout
        self.progress = "idle"
        self.tid_list = []
        self.date_created = str(datetime.now())
        
    def getSize(self):
        return len(self.urls)
        
    def printTask(self):
        return json.dumps(self.__dict__)
        