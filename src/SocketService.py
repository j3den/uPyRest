# This Service once started listens on the set port for HTTP requests.
#
# HTTP Request format lines:
# 0: Request Type (GET/POST/PATCH/DELETE) 	b'POST / HTTP/1.1'
# A blank line is followed by the body.
# the body ends with a '
import socket
import repos.POST as postrepo
import display.DisplayServiceSingleton as ds


def init():
    print("Setting up WebSocket -> Binding Socket to 80...")
    display = ds.DisplaySingleService()
    print_text = display.print_text
    clear_display = display.clear
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)
    print("Socket on port 80 bound")

    while True:
        conn, addr = s.accept()

        sender_ip = str(addr[0])
        while len(sender_ip) < 13:
            sender_ip = " " + sender_ip + " "
        sender_ip = "!" + sender_ip + "!"

        try:
            logString = ""
            request = conn.recv(1024)
            request = str(request)
            parts = request.split("\\r\\n")
            clear_display()
            print_text("!!!!!!!!!!!!!!!!", 0)
            print_text(sender_ip, 2)
            print_text("!              !", 3)
            print_text("!              !", 4)
            print_text("!!!!!!!!!!!!!!!!", 5)

            if "POST" in parts[0]:
                print_text("!     POST     !", 1)
                logString = logString + str(addr) + " POST "
                try:
                    print(str(postrepo.persist(request)))
                    conn.send("HTTP/1.1 201 Created\n" + "Content-Type: text/html\n"
                    + "\n\n" + "201 CREATED")  # Important!
                except Exception as e:
                    print(str(e))
                    conn.send("HTTP/1.1 500 Internal Server error\n" + "Content-Type: text/html\n"
                              + "\n\n" + "500 Internal Server error")  # Important!



            if "GET" in parts[0]:
                print_text("!      GET     !", 1)
                logString = logString + str(addr) + " GET "
                conn.send("HTTP/1.1 200 OK\n" + "Content-Type: text/html\n"
                          + "\n" + "OK GET")  # Important!
                conn.close()
                print(logString)

            conn.close()
        except Exception as e:
            print(str(e))
