from socket import socket, AF_INET, SOCK_DGRAM
import time

s = socket(AF_INET, SOCK_DGRAM)
ip_dest = '192.168.42.203'
port_dest = 12345
for i in range(11):
    msg = 'A'
    s.sendto(msg, (ip_dest, port_dest))
    s.sendto(msg, (ip_dest, port_dest))
    time.sleep(2)
    data, sender_info = s.recvfrom(2048)
    print(data)
# Print the response from the server and close the socket.
data, sender_info = s.recvfrom(2048)
print "Server sent: ", data
s.close()

