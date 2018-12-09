import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_dest = '0.0.0.0'
port_dest = 12345
server.bind((ip_dest, port_dest))
server.listen(5)
# Accept a new client and handle it.
client_socket, client_address = server.accept()
print 'Connection from: ', client_address
data = "hi"  # Dummy initial value
a_counter = 0  # This counter remembers how many 'A's were sent so far.
while data != '':  # The client will send '' if it closes.
    data = client_socket.recv(1024)
    client_socket.send('B')
    if data == 'A':  # Message is one A
        a_counter += 1
    elif data == 'AA':  # Message is two 'A's
        a_counter += 2
    print 'Received:', data
    # If we received 22 'A's, which is the amount expected, we can stop the loop.
    if a_counter == 22:
        break
# Answer B and close both sockets
print 'Client disconnected'
client_socket.close()
server.close()