# Created by: Micah Cinco
# Version 1. October 2014

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep
import cgi, json, mongo, pprint, re
from task import Task
from bson.json_util import dumps

PORT_NUMBER = 8080

class myHandler(BaseHTTPRequestHandler):
	"""Handles all GET and POST requests from
		the browser."""
	
	# Handler for the GET requests
	def do_GET(self):
		if self.path == "/":
			self.path = "/index.html"
		elif self.path == "/create?":
			self.path = "/create.html"
		elif self.path == "/delete?":
			self.path = "/delete.html"

		try:
			# Check the file exists
			sendReply = False
			if self.path.endswith(".html"):
				mimetype = 'text/html'
				sendReply = True

			if sendReply == True:
				# Open the static file requested and send it
				f = open(curdir + sep + self.path) 
				self.send_response(200)
				self.send_header('Content-type', mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
			return
		except IOError:
			self.send_error(404, 'File Not Found: %s' % self.path)

	# Handler for the POST requests
	def do_POST(self):
		# Create a Task
		if self.path == "/send":
			form = cgi.FieldStorage(
				fp=self.rfile,
				headers=self.headers,
				environ={'REQUEST_METHOD':'POST',
		                 'CONTENT_TYPE':self.headers['Content-Type'],
			})

			data = form.getvalue("urls")
			urls = [x.strip() for x in re.split(' |,|\n', data)]
			timeout = form.getvalue("timeout")
			priority = form.getvalue("priority")
			
			t = Task(urls, timeout, priority)
			self.send_response(200)
			self.end_headers()
			
			obj_id = mongo.push_task(t)
			self.wfile.write("Task pushed to DB successfully.\nObjectID is %s" % obj_id)
			return
		
		# Check Tasks
		elif self.path == "/check":
			form = cgi.FieldStorage(
				fp=self.rfile,
				headers=self.headers,
				environ={'REQUEST_METHOD':'POST',
		                 'CONTENT_TYPE':self.headers['Content-Type'],
			})
			
			progress = form.getvalue("progress")
			if progress == None:
				self.wfile.write("<h1>No progress selected\n</h1>")
				return
			self.send_response(200)
			self.end_headers()
			self.wfile.write(dumps(mongo.check_tasks(progress), indent=2, sort_keys=True))
			self.wfile.write(mongo.print_size(progress))
			return

		# Delete Tasks (by progress or ID)
		elif self.path == "/delete":
			form = cgi.FieldStorage(
				fp=self.rfile,
				headers=self.headers,
				environ={'REQUEST_METHOD':'POST',
		                 'CONTENT_TYPE':self.headers['Content-Type'],
			})
			
			progress = form.getvalue("progress")
			if progress == None:
				taskid = form.getvalue("deleteID")
				if taskid == None:
					self.wfile.write("<h1>No progress or Task ID entered.\n</h1>")
					return
				else:
					self.wfile.write(mongo.delete_task(taskid))
					return
			
			else:
				if mongo.get_progress_size(progress) == 0:
					self.wfile.write("<h1>No tasks to delete in selected progress state.\n</h1>")
					return
				else:
					self.wfile.write("<h1>Successfully deleted tasks.\n</h1>")
					self.wfile.write(mongo.delete_progress(progress))
					return
		
try:
	# Create a web server and define the handler to manage the
	# incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	# Wait forever for incoming http requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()