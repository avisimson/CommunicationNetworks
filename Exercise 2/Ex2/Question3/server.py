import socket, threading

# data directory, server ip and port and http msg.
data_directory = "files"
ip = '127.0.0.1'
port = 25000
max_clients = 10
HTTP_OK = "HTTP/1.1 200 OK\r\nConnection: close\r\n\r\n{content}"
HTTP_Not_Found = "HTTP/1.1 404 Not Found\r\nConnection: close"
HTTP_Moved = "HTTP/1.1 301 Moved Permanently\r\nConnection: close\r\nLocation: /result.html\r\n\r\n"


"""
function get a file request and try to find, read and return its content.
(if not found or fail to read return empty content).
param request_address is the requested name of file that the client wants.
"""
def find_file(request_address):
    path = data_directory + "/" + request_address
    try:
        if request_address.endswith(".jpg"):
            # case of reading picture.
            requested_file = open(path, "rb")
        else:
            # case of reading a text file.
            requested_file = open(path, "r")
        # reading the file content and closing it.
        result = requested_file.read()
        requested_file.close()
        return result
    except:  # file not found-return empty msg.
        return ""


"""
Handling the client requests.
param client_socket is the socket of the client.
"""
def handle_client(client_socket):
    message = client_socket.recv(1024)
    print(message)
    split = message.split("\r\n")
    # get the first line. the GET request.
    client_request = split[0].split(" ")
    # put not found that will change if we find the requested item.
    answer = HTTP_Not_Found
    if client_request[0] == "GET":
        request_address = client_request[1]
        # case of redirect
        if request_address == "/redirect":
            answer = HTTP_Moved
        else:
            # case of request to file.
            if request_address == "/":  # Handling the index.html case.
                request_address = "index.html"
            # try to find the file in the directory and change to http_ok and the file if found.
            # present not found if result is null.
            result = find_file(request_address)
            if result:
                answer = HTTP_OK.format(content=result)
    # send info answer to client
    client_socket.send(answer)
    print answer
    # close connection with current client.
    client_socket.close()

# main


# server creation.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ip, port))
server_socket.listen(max_clients)
# listening and accepting client connections.
while True:
    client_socket, client_address = server_socket.accept()
    print 'New Connection: ', client_address
    # handling new client.
    threading.Thread(target=handle_client, args=[client_socket]).start()
