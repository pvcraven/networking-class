# Import the built-in library that manages network sockets
import socket

# What IP address do you want to listen on?
listen_ip_address = '192.168.1.101'

# What port might the message come in on?
listen_ip_port = 10000

# How big might the message be?
buffer_size = 65000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((listen_ip_address, listen_ip_port))
# s.setblocking(0)

while True:
    data, source_address = s.recvfrom(1024)
    print("From {}:{}: {}".format(source_address[0], source_address[1], data))
