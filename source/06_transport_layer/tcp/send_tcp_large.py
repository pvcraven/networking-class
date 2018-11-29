import socket

# IP address and port of where we'll send the message.
server_ip_address = '127.0.0.1'
server_ip_port = 5005

# Size of our message.
# Must be at least 1
message_size_in_bytes = 300000

# Message as a byte array. (Hence the b at the front.)
# Send a bunch of x's, and an "END"
my_message = b"X" * (message_size_in_bytes - 1) + b"\n"

try:
  # Open a socket
  my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Connect to this server, and this port.
  my_socket.connect((server_ip_address, server_ip_port))

  # Send the message
  my_socket.sendall(my_message)

  # Close the socket
  my_socket.close()

except:
  # Something bad happened.
  print("Unable to send the message.")

print("Done")
