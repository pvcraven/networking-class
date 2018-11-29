import time
import socket

# IP address and port of where we'll send the message.
server_ip_address = '10.1.23.175'
server_ip_port = 5005

def send_data(total_bytes, message_size_in_bytes):

    # Total number of messages to send.
    messages_to_send = total_bytes // message_size_in_bytes

    # Message as a byte array. (Hence the b at the front.)
    # Send byte array with an X:   b"X"
    # Repeat this (message_size_in_bytes - 1) times.
    # Pop a \n at the end.
    my_message = b"X" * (message_size_in_bytes - 1) + b"\n"

    # Open a socket
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

    # Connect to this server, and this port.
    my_socket.connect((server_ip_address, server_ip_port))

    # Repeat, and send our message over and over.
    for i in range(messages_to_send):
        my_socket.sendall(my_message)

    # Send a message signaling we are done sending packets.
    my_socket.send(b"Y\n")

    # Close the socket
    my_socket.close()

    # print("Done")

def main():
    # How many bytes to send
    """
    total_bytes = 5000000

    for message_size_in_bytes in range(25, 0, -1):
        print("Sending {:,} bytes in {} byte chunks.".format(total_bytes, message_size_in_bytes))
        send_data(total_bytes, message_size_in_bytes)
    """

    total_bytes = 10
    message_size_in_bytes = 10
    for message_size_in_bytes in range(500000):
        print("Sending {:,} bytes in {} byte chunks.".format(total_bytes, message_size_in_bytes))
        send_data(total_bytes, message_size_in_bytes)

main()
