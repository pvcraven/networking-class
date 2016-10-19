import socket
import time

BUFFER_SIZE = 65535

# Receive info
my_ip_address = '10.1.23.175'
my_ip_port = 5005

def main():
    # Our full message. Right now it is blank.
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

                # Start timing how long this takes.
                start_time = time.clock()

            except BlockingIOError:
                pass

        # If we have a connection, receive data
        if state == CONNECTED:
            try:
                # Read in the data, up to the number of characters in BUFFER_SIZE
                data = connection.recv(BUFFER_SIZE)
                chunks += 1

                # Enable this if you want to see the data. But it will throw
                # off our timings if we do this.

                # if len(data) > 0:
                #     print("Data from {}:{} \"{}\"".format(client_address[0], client_address[1], data))

                # Append this chunk to the full message
                full_message += data

                if full_message[-2] == 89:

                    # Stop timing how long this takes.
                    end_time = time.clock()

                    # Close the socket. No socket operations can happen after this.
                    state = NO_CONNECTION
                    connection.close()
                    done = True

            except BlockingIOError:
                pass

    # Close the socket. No socket operations can happen after this.
    my_socket.close()

    # Calculate our results
    total_bytes = len(full_message)
    total_time = end_time - start_time
    data_rate = total_bytes / total_time

    # Print our results
    print("Processed {:,} bytes in {:,} chunks.".format(total_bytes, chunks))
    print("Total time: {:.3f} seconds.".format(total_time))
    print("Data rate: {:,.0f} bytes/second.".format(data_rate))


main()
