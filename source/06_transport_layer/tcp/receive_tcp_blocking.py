import socket

# This is your buffer. You can't receive anything more than this at
# one time.
BUFFER_SIZE = 65535

my_ip_address = '127.0.0.1'
my_ip_port = 5005

# Create a socket for sending/receiving data
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tell the socket it will be listening on my_ip_address, and my_port.
my_socket.bind((my_ip_address, my_ip_port))

# We are going to be listening as a server, not connecting as a client.
# The "1" specifies the size of the backlog of connections we allow before
# refusing connections.
my_socket.listen(1)

while True:

  try:
    # Get a connection, and the address that hooked up to us.
    # The 'client address' is an array that has the IP and the port.
    connection, client_address = my_socket.accept()

    # Read in the data, up to the number of characters in BUFFER_SIZE
    data = connection.recv(BUFFER_SIZE)

    # Print what we read in, and from where
    print("Data from {}:{} \"{}\"".format(client_address[0], client_address[1], data))

  except:
    # Whoa Nelly! Was there an error?
    print("Unable to receive the message.")

  finally:
    # Close the socket. No socket operations can happen after this.
    # If there was more data to send, you would not want to do this.
    # You would want a loop of 'recv' and keep the 'accept' and 'close'
    # out of that loop.
    connection.close()

socket.close()

print("Done")
