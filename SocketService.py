#Creates the socket for incoming requests.

#HTTP Request format lines:
#0: Request Type (GET/POST/PATCH/DELETE) 	b'POST / HTTP/1.1'
# A blank line is followed by the body.
# the body ends with a '...strip it.
import socket
def init():
	print("Setting up WebSocket -> Binding Socket to 80...")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('', 80))
	s.listen(5)
	print("Socket on port 80 bound")
	while True:
		logString = ""
		conn, addr = s.accept()
		request = conn.recv(1024)
		request = str(request)
		parts = request.split("\\r\\n")
		if("POST" in parts[0]):
			logString=logString+str(addr)+" POST :"
			for i in range(0,len(parts)):
				if(str(parts[i]) == ""):
					logString = logString + str(parts[i+1][:-1]) + "\n"
		print(logString)
		conn.send("HTTP/1.1 201 Created\n"+"Content-Type: text/html\n"
         	+"\n") # Important!
		conn.close()
