import socket

BUFFER_SIZE = 65535

my_ip_address = '127.0.0.1'
my_ip_port = 5005

# Our full message
full_message = b""

# We need to build a "state machine" that keeps
# track of if we are connected or not
NO_CONNECTION = 1
CONNECTED = 2

state = NO_CONNECTION

# Create a socket for sending/receiving data
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Make the socket non-blocking
my_socket.settimeout(0.0)

# Tell the socket it will be listening on my_ip_address, and my_port.
my_socket.bind((my_ip_address, my_ip_port))

# We are going to be listening as a server, not connecting as a client.
# The "1" specifies the size of the backlog of connections we allow before
# refusing connections.
my_socket.listen(1)

done = False
chunks = 0

while not done:

    # If we have no connection, then see if we can build a connection
    if state == NO_CONNECTION:
        try:
            # Get a connection, and the address that hooked up to us.
            # The 'client address' is an array that has the IP and the port.
            connection, client_address = my_socket.accept()
            state = CONNECTED
        except BlockingIOError:
            pass

    # If we have a connection, receive data
    if state == CONNECTED:
        try:
            # Read in the data, up to the number of characters in BUFFER_SIZE
            data = connection.recv(BUFFER_SIZE)
            chunks += 1

            if len(data) > 0:
                print("Data from {}:{} \"{}\"".format(client_address[0], client_address[1], data))

            # Append this chunk to the full message
            full_message += data

            if full_message[-1] == 10:
                # Close the socket. No socket operations can happen after this.
                state = NO_CONNECTION
                connection.close()
                done = True

        except BlockingIOError:
            pass

# Close the socket. No socket operations can happen after this.
my_socket.close()

print("Done receiving message. Processed {} bytes in {} chunks.".format(len(full_message), chunks))
