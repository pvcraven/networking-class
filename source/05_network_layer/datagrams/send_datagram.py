# Import the built-in library that manages network sockets
import socket

# Address of the target. Replace this with the address that you want.
destination_ip_address = '127.0.0.1'

# Port to send the packet to.
destination_ip_port = 10000

# Enter the data content of the UDP packet as an array of
# bytes. That's why there is a 'b' in front of the string.
packet_data = b'This is a test message.'

# Initialize a network socket
# SOCK_DGRAM specifies that this is UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

# Connect the socket. For UDP this doesn't send anything yet. It does say
# that when we do send data, where will it go.
s.connect((destination_ip_address, destination_ip_port))

# Send the data.
s.send(packet_data)

# Close the socket. Let someone else use it.
s.close()
