from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep
import cgi, json, mongo, pprint, re
from task import Task
from bson.json_util import dumps

PORT_NUMBER = 8080

# This class will handles any incoming request from
# the browser 
class myHandler(BaseHTTPRequestHandler):
	
	# Handler for the GET requests
	def do_GET(self):
		if self.path == "/":
			self.path = "/index.html"
		elif self.path == "/createtask?":
			self.path = "/create.html"
		elif self.path == "/results?":
			self.path = "/results.html"

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
		
		elif self.path == "/results":
			form = cgi.FieldStorage(
				fp=self.rfile,
				headers=self.headers,
				environ={'REQUEST_METHOD':'POST',
		                 'CONTENT_TYPE':self.headers['Content-Type'],
			})
			
			progress = form.getvalue("progress")
			self.send_response(200)
			self.end_headers()
			self.wfile.write(dumps(mongo.check_tasks(progress), indent=2, sort_keys=True))
			self.wfile.write(mongo.print_size(progress))
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
