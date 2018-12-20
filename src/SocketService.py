# This Service once started listens on the set port for HTTP requests.
#
# HTTP Request format lines:
# 0: Request Type (GET/POST/PATCH/DELETE) 	b'POST / HTTP/1.1'
# A blank line is followed by the body.
# the body ends with a '
import socket
import repos.POST as postRepoService
import repos.GETRepo as getRepoService
import repos.DELETERepo as deleteRepoService
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
    postRepo = postRepoService.PostRepo()
    getRepo = getRepoService.GetRepo()
    deleteRepo = deleteRepoService.DeleteRepo()

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
                    postRepo.persist(request)
                    conn.send("HTTP/1.1 201 Created\n" + "Content-Type: text/html\n"
                              + "\n\n" + "201 CREATED")  # Important!
                except Exception as e:
                    print(str(e))
                    conn.send("HTTP/1.1 500 Internal Server error\n" + "Content-Type: text/html\n"
                              + "\n\n" + "500 Internal Server error")  # Important!

                conn.close()

            if "GET" in parts[0]:
                print_text("!      GET     !", 1)
                getRepo.getAll(request, conn)
                logString = logString + str(addr) + " GET "
                print(logString)

            if "DELETE" in parts[0]:
                print_text("!    DELETE   !", 1)
                deleteRepo.deleteAll(request, conn)
                logString = logString + str(addr) + " DELETE "
                print(logString)

        except Exception as e:
            print(str(e))
