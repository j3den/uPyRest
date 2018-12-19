# This Service once started listens on the set port for HTTP requests.
#
#HTTP Request format lines:
#0: Request Type (GET/POST/PATCH/DELETE) 	b'POST / HTTP/1.1'
# A blank line is followed by the body.
# the body ends with a '
import socket
import repos.POST as postrepo
import display.DisplayServiceSingleton as ds



def init():
	print("Setting up WebSocket -> Binding Socket to 80...")
	display = ds.DisplaySingleService()
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('', 80))
	s.listen(5)
	print("Socket on port 80 bound")
	while True:
		try:
			logString = ""
			conn, addr = s.accept()
			request = conn.recv(1024)
			request = str(request)
			parts = request.split("\\r\\n")

			if("POST" in parts[0]):
				logString=logString+str(addr)+" POST "
				response = postrepo.persist(request)
				conn.send("HTTP/1.1 201 Created\n"+"Content-Type: text/html\n"
         			+"\n"+response) # Important!
				conn.close()
				print(logString)

				display.print_text(str(addr),3)
				display.print_text("     POSTr     ", 4)

		
			if("GET" in parts[0]):
				logString=logString+str(addr)+" GET "
				conn.send("HTTP/1.1 200 OK\n"+"Content-Type: text/html\n"
         			+"\n"+"OK GET") # Important!
				conn.close()
				print(logString)

				display.print_text(str(addr), 3)
				display.print_text("     GET     ", 4)


		except:	
			conn.send("HTTP/1.1 400 Bad Request\n"+"Content-Type: text/html\n"
         		+"\n"+"ERROR") # Important!
			conn.close()
			print(logString)
		

