from socket import socket, AF_INET, SOCK_DGRAM

server = socket(AF_INET, SOCK_DGRAM)
server_ip = '0.0.0.0'
server_port = 12345
server.bind((server_ip, server_port))

data = "hi"
a_counter = 0
while data != '':
    data, sender_info = server.recvfrom(1024)
    server.sendto('B', sender_info)
    if data == 'A':
        a_counter += 1
    elif data == 'AA':
        a_counter += 2
    print('Received:', data)
    if a_counter == 22:
        break
server.close()
