# Import the built-in library that manages network sockets
import socket
import time

# What IP address do you want to listen on?
listen_ip_address = '10.1.23.175'

# What port might the message come in on?
listen_ip_port = 10000

# How big might the message be?
buffer_size = 65000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((listen_ip_address, listen_ip_port))

# Set the socket to non-blocking. If we have no data, don't wait for it.
s.setblocking(0)

while True:
    try:
        data, source_address = s.recvfrom(1024)
        print("From {}:{}: {}".format(source_address[0], source_address[1], data))

    except BlockingIOError:
        # We didn't get any data. Wait and then try again
        time.sleep(0.1)

