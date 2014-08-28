import json

class Task(object):
    urls = []
    priority = ""

    # The class "constructor" 
    def __init__(self, urls, priority):
        self.urls = urls
        self.priority = priority
        self.timeout = 100
        self.isCompleted = False

    def getURLS(self):
        return self.urls
        
    def getPriority(self):
        return self.priority
        
    def getTimeout(self):
        return self.timeout
        
    def getSize(self):
        return len(self.urls)
        
    def getStatus(self):
        if self.isCompleted == False:
            return "Not Completed"
        elif self.isCompleted == True:
            return "Completed"
        
    def printTask(self):
        return json.dumps(self.__dict__)
        #return "URL(s): %s\n" % self.getURLS(), "Priority: %s\n" % self.getPriority(), '\nTimeout: ', self.getTimeout(), '\nSize: ', self.getSize(), '\nStatus: ', self.getStatus()
        