import sys  # Import sys to access command line arguments
from socket import *  # Import socket module for network connections

if len(sys.argv) != 4:  # Check if the correct number of arguments are provided
    print("Usage: python3 client.py server_host server_port filename")
    sys.exit()  # Exit if the incorrect number of arguments are given

# Assign command line arguments to variables for easier access
serverHost = sys.argv[1]
serverPort = int(sys.argv[2])
filename = sys.argv[3]

# Create a TCP/IP client socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to the server using the provided host and port
clientSocket.connect((serverHost, serverPort))

# Format the GET request string using the provided filename
getRequest = f"GET /{filename} HTTP/1.1\r\nHost: {serverHost}\r\n\r\n"

# Send the GET request to the server
clientSocket.send(getRequest.encode())

# Receive and print the response from the server
response = clientSocket.recv(4096).decode()
print("Server response:\n", response)

# Close the client socket
clientSocket.close()

