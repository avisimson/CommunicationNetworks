from socket import socket, AF_INET, SOCK_DGRAM
import sys

#check the arguments to program.
if len(sys.argv) != 3:
    print "wrong number of arguments, forced to exit."
    sys.exit(0)

#get the server port and ip from args.
server_ip = sys.argv[1]
server_port = int(sys.argv[2])

#create socket to networking
s = socket(AF_INET, SOCK_DGRAM)

#connect to server and send requests for ip's of websites.
msg = raw_input("Enter website: (or quit if you want to disconnect) \n")
while not msg == 'quit':
    s.sendto(msg, (server_ip,server_port))
    data, sender_info = s.recvfrom(2048)
    print "Server's answer to ip of the website: ", data
    msg = raw_input("Enter website: (or quit if you want to disconnect) \n")
s.close()
