# Created by: Micah Cinco
# Version 1. October 2014

import json
from datetime import datetime


class Task(object):
	"""Task object"""
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
    	"""Returns the number of URLs in the Task.
    	@return len(self.urls)"""
        return len(self.urls)
        
    def printTask(self):
    	"""Returns the Task in JSON format as a string.
    	@return task.__dict__"""
        return json.dumps(self.__dict__)
        