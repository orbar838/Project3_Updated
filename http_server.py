from http.server import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep
import cgi

PORT_NUMBER = 8081

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		if self.path=="/":
			self.path="/index.html"

		try:
			#Check the file extension required and
			#set the right mime type

			sendReply = False
			if self.path.endswith(".html"):
				mimetype='text/html'
				sendReply = True
			if self.path.endswith(".jpg"):
				mimetype='image/jpg'
				sendReply = True
			if self.path.endswith(".gif"):
				mimetype='image/gif'
				sendReply = True
			if self.path.endswith(".png"):
				mimetype='image/png'
				sendReply = True
			if self.path.endswith(".js"):
				mimetype='application/javascript'
				sendReply = True
			if self.path.endswith(".css"):
				mimetype='text/css'
				sendReply = True

			if sendReply == True:
				self.handle_http(mimetype)
				return

		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)

	def handle_http(self, mime_type):
		try:
			f = open(curdir + sep + self.path, 'rb')
			self.send_response(200)
			self.send_header('Content-type',mime_type)
			self.end_headers()
			self.wfile.write(f.read())
			f.close()
			
		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)		
			
	def do_POST(self):
		if self.path=="/":
			form = cgi.FieldStorage(
				fp=self.rfile, 
				headers=self.headers,
				environ={'REQUEST_METHOD':'POST',
		                 'CONTENT_TYPE':self.headers['Content-Type'],
			})
			for i in form:
				print (i, form[i])
			if "email" in form:
				email_addr = form["email"].value
				text = "Thanks %s !" % email_addr
			else:
				text = "You didn\'t types any email address"
			print (text)
			self.send_response(200)
			self.end_headers()
			text_res = bytes(text, 'utf-8')
			self.wfile.write(text_res)
			return
			
		elif self.path=="/html5_form":
			form = cgi.FieldStorage(
				fp=self.rfile, 
				headers=self.headers,
				environ={'REQUEST_METHOD':'POST',
		                 'CONTENT_TYPE':self.headers['Content-Type'],
			})
			for i in form:
				print (i, form[i])
			if "html5_email" in form:
				email_addr = form["html5_email"].value
				text = "Thanks %s !" % email_addr
			else:
				text = "You didn\'t types any email address"
			print (text)
			self.send_response(200)
			self.end_headers()
			text_res = bytes(text, 'utf-8')
			self.wfile.write(text_res)
			return

			
try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print ('Started httpserver on port ' , PORT_NUMBER)
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print ('^C received, shutting down the web server')
	server.socket.close()