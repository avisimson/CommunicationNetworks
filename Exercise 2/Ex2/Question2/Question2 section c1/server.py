from socket import socket, AF_INET, SOCK_DGRAM

server = socket(AF_INET, SOCK_DGRAM)
server_ip = '0.0.0.0'
server_port = 12345
server.bind((server_ip, server_port))

data, sender_info = server.recvfrom(20000)
print('Connection from: ', sender_info)
print('Received: ', data)
server.sendto('B', sender_info)
server.close()
