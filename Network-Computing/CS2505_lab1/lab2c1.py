from socket import *
import sys

# Check if the command line arguments are less than 3 (script name, server_ip, port).
if len(sys.argv) < 3:
    print("Usage: python client_2.py <server_ip> <port>")
    sys.exit(1)  # Exit the script if the required arguments are not provided.

# Assign the second command line argument to server_ip.
server_ip = sys.argv[1]
# Convert the third command line argument to an integer and assign it to port_number.
port_number = int(sys.argv[2])
print("Connecting to server at %s on port %s" % (server_ip, port_number))

# Create a TCP/IP socket.
sock = socket(AF_INET, SOCK_STREAM)
server_address = (server_ip, port_number)  # Define the server address using the IP and port number.
sock.connect(server_address)  # Establish a connection to the server.

try:
    # Prompt the user for a message to send to the server.
    message = input("Enter the message to send to the server: ")
    print('sending "%s"' % message)  # Indicate what message is being sent.
    sock.sendall(message.encode())  # Send the message to the server after encoding it to bytes.
    
    amount_received = 0  # Initialize the amount of data received from the server.
    amount_expected = len(message)  # Set the expected amount of data (which should match the message length).
    
    while amount_received < amount_expected:
        # Receive data from the server in 64-byte chunks.
        data = sock.recv(64).decode()
        amount_received += len(data)  # Update the amount received based on the data length.
        print('received "%s"' % data)  # Print out what was received from the server.
finally:
    sock.close()  # Ensure the socket is closed when done.
    print('Socket closed.')  # Indicate that the socket has been closed.
