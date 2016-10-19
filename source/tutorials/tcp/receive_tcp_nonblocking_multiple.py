import socket
import time

BUFFER_SIZE = 65535

# Receive info
my_ip_address = '10.1.23.175'
my_ip_port = 5005

# We need to build a "state machine" that keeps
# track of if we are connected or not
NO_CONNECTION = 1
CONNECTED = 2

class MyConnectionHandler:
    """
    Handle receiving data
    """

    def __init__(self):
        """
        Initialize the class
        """
        self.my_socket = None
        self.state = NO_CONNECTION

    def start_listening(self):
        """
        Open the socket for listening
        """
        # Create a socket for sending/receiving data
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Make the socket non-blocking
        self.my_socket.settimeout(0.0)

        # Tell the socket it will be listening on my_ip_address, and my_port.
        self.my_socket.bind((my_ip_address, my_ip_port))

        # We are going to be listening as a server, not connecting as a client.
        # The "2" specifies the size of the backlog of connections we allow before
        # refusing connections.
        self.my_socket.listen(2)

    def handle_connection(self):
        """
        Manage a connected socket
        """
        # Our full message. Right now it is blank.
        full_message = b""

        done = False
        chunks = 0

        while not done:

            # If we have no connection, then see if we can build a connection
            if self.state == NO_CONNECTION:
                try:
                    # Get a connection, and the address that hooked up to us.
                    # The 'client address' is an array that has the IP and the port.
                    connection, client_address = self.my_socket.accept()
                    self.state = CONNECTED

                    # Start timing how long this takes.
                    start_time = time.clock()

                except BlockingIOError:
                    pass

            # If we have a connection, receive data
            if self.state == CONNECTED:
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

                    # Check for a Y instead of an X. This means that we have the
                    # last packet, and we are done.
                    if full_message[-2] == 89:

                        # Stop timing how long this takes.
                        end_time = time.clock()

                        # Close the socket. No socket operations can happen after this.
                        self.state = NO_CONNECTION
                        connection.close()
                        done = True

                except BlockingIOError:
                    pass


        # Calculate our results
        total_bytes = len(full_message)
        total_time = end_time - start_time
        data_rate = total_bytes / total_time

        # Print our results
        # If you are graphing this, you might want to change the output to be
        # easier to get into Excel.
        print("Processed {:,} bytes in {:,} chunks.".format(total_bytes, chunks))
        print("Total time: {:.3f} seconds.".format(total_time))
        print("Data rate: {:,.0f} bytes/second.".format(data_rate))
        print()

    def stop_listening(self):
        # Close the socket. No socket operations can happen after this.
        self.my_socket.close()

def main():
    """
    Main program
    """
    my_connection_handler = MyConnectionHandler()
    my_connection_handler.start_listening()

    while True:
        my_connection_handler.handle_connection()

    # Ok, we don't actually get here. But if we did, this is how you'd
    # properly shut down.
    my_connection_handler.stop_listening()

main()
