# Import necessary libraries
import sys
from socket import *

# Check if the correct number of arguments are provided
if len(sys.argv) != 6:
    print("Usage: python3 test_client.py server_host server_port method filename http_version")
    sys.exit()

# Assign command line arguments to variables
serverHost = sys.argv[1]
serverPort = int(sys.argv[2])
method = sys.argv[3]  # GET, POST, etc.
filename = sys.argv[4]
http_version = sys.argv[5]  # HTTP/1.1, HTTP/2, etc.

# Create a TCP/IP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect the socket to the server's address and port
clientSocket.connect((serverHost, serverPort))

# Construct the request message for the specified file
request = f"{method} /{filename} {http_version}\r\nHost: {serverHost}\r\n\r\n"

# Send the request to the server
clientSocket.send(request.encode())

# Receive the response from the server and decode it
response = clientSocket.recv(4096).decode()

# Print the response
print("Server response:\n", response)

# Close the socket
clientSocket.close()
