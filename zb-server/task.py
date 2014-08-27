class Task(object):
    urls = []
    priority = ""

    # The class "constructor" 
    def __init__(self, urls, priority):
        self.urls = urls
        self.priority = priority
        self.timeout = 100

def make_task(urls, priority, timeout):
    task = Task(urls, priority, timeout)
    return task
