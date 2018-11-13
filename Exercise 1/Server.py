from socket import socket, AF_INET, SOCK_DGRAM
import sys

#arg: the name of the file
#returns: dictionary of all sites with their ip's from file.
def file_to_dictionary(file_name):
    try:
        file1 = open(file_name,"r")
    except:
        print "error in opening file, abort"
        sys.exit(0)
    dictionary = {}
    for line in file1:
        web_ip = line.split(",")
        dictionary.update({web_ip[0] : web_ip[1]})
    file1.close()
    return dictionary

#child server connects to parent server and get the info from him.
#args- the port of parent server, and msg = website address from client.
def connect_to_parent(parent_port, msg):
    s = socket(AF_INET, SOCK_DGRAM)
    print "sending " + msg + " to parent server"
    s.sendto(msg, ('127.0.0.1',parent_port))
    data, sender_info = s.recvfrom(2048)
    print "parent sent " + data
    return data


#check the arguments to the program.
if len(sys.argv) != 5:
    print "wrong number of arguments, forced to exit."
    sys.exit(0)

#parse info from arguments to program.
parent_ip = sys.argv[2]
my_port = int(sys.argv[1])
parent_port = int(sys.argv[3])
file_name = sys.argv[4]
my_ip = parent_ip

#create socket for networking.
s = socket(AF_INET, SOCK_DGRAM)
try:
    s.bind((my_ip, my_port))
except:
    try:
        s.bind(('127.0.0.1', my_port))
    except:
        print "failed to bind, abort \n"
        sys.exit(0)

#create dictionary according to file.
dictionary = file_to_dictionary(file_name)

#run service
while True:
    print "wait for messages"
    msg, sender_info = s.recvfrom(2048)
    print "Message: ", msg, " from: ", sender_info

    #check if input is in dictionary.
    if msg in dictionary:
        s.sendto(dictionary[msg], sender_info)
    else:
        #get the info from the parent server.
        data = connect_to_parent(parent_port, msg)
        dictionary.update({msg : data})
        s.sendto(dictionary[msg], sender_info)
