import json

class Task(object):
    urls = []
    priority = ""
    timeout = 100

    # The class "constructor" 
    def __init__(self, urls, timeout, priority):
        self.urls = urls
        self.priority = priority
        self.timeout = timeout
        self.isCompleted = False
        self.status = None
        
    def getSize(self):
        return len(self.urls)
        
    def printTask(self):
        return json.dumps(self.__dict__)
        