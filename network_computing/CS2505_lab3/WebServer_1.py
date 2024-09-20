# Import socket module
from socket import *

# Create a TCP server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 6789

# Bind the socket to server address and server port
serverSocket.bind(("", serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(1)

print('The server is ready to receive')

# Server should be up and running and listening to the incoming connections
while True:
    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()
    
    try:
        message = connectionSocket.recv(1024).decode()
        requestParts = message.split(' ')
        
        # Validate the request method
        if requestParts[0] != 'GET':
            # If not GET, send a 400 Bad Request response
            response = "HTTP/1.1 400 Bad Request\r\n\r\n"
            connectionSocket.send(response.encode())
            connectionSocket.close()
            continue  # Skip further processing and wait for the next connection
        
        # Validate the HTTP version
        if "HTTP/1.1" not in requestParts[2]:
            # If not HTTP/1.1, send a 505 HTTP Version Not Supported response
            response = "HTTP/1.1 505 HTTP Version Not Supported\r\n\r\n"
            connectionSocket.send(response.encode())
            connectionSocket.close()
            continue  # Skip further processing and wait for the next connection
    
    # Existing file handling code follows...

        
        # Extract the path of the requested object from the message
        filename = message.split()[1]
        with open(filename[1:], 'r') as f:
            outputdata = f.read()
        
        # Send one HTTP header line into socket
        header = "HTTP/1.1 200 OK\r\n\r\n"
        connectionSocket.send(header.encode())
        
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        header = "HTTP/1.1 404 Not Found\r\n\r\n"
        connectionSocket.send(header.encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        
        # Close client socket
        connectionSocket.close()

serverSocket.close()
