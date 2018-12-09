import socket, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest_ip = '192.168.42.203'
dest_port = 12345
s.connect((dest_ip, dest_port))

for i in range(11):
    msg = 'A'
    s.send(msg)
    s.send(msg)
    time.sleep(2)
    data = s.recv(4096)
    print(data)

data = s.recv(4096)
print("Server sent: ", data)
s.close()