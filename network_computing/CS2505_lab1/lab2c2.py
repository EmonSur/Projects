# from the socket module import all
from socket import *
import sys

# Check if the correct number of command-line arguments were provided
# The first argument is the script name, the second should be the server's IP address, and the third should be the port number
if len(sys.argv) < 3:
    print("Usage: python client_2.py <server_ip> <port>")
    sys.exit(1)  # Exit the program if the arguments are not sufficient

# Retrieve the server IP and port number from the command-line arguments
server_ip = sys.argv[1]  # The server's IP address is the second argument
port_number = int(sys.argv[2])  # The port number is the third argument and converted to an integer
print("Connecting to server at %s on port %s" % (server_ip, port_number))

# Create a TCP socket using IPv4 addressing
sock = socket(AF_INET, SOCK_STREAM)
server_address = (server_ip, port_number)  # Combine the server IP and port into a tuple

# Establish a connection to the server at the specified address
sock.connect(server_address)

try:
    while True:  # Start an infinite loop to send messages repeatedly
        message = input("You: ")  # Take input from the user to send to the server
        if message.lower() == 'exit':  # If the user types 'exit', break out of the loop
            break

        # Send the input message to the server
        sock.sendall(message.encode())  # Encode the string to bytes before sending

        # Wait and receive the response from the server
        # The argument to recv specifies the maximum amount of data to be received at once
        data = sock.recv(2048).decode()  # Decode the bytes back into a string
        print('Server:', data)  # Print the server's response

# Once out of the loop, close the socket to clean up the resources
finally:
    print('Closing socket')
    sock.close()
