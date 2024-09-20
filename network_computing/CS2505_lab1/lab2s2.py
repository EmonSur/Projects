# from the socket module import all
from socket import *
import sys

# The sys module is used for accessing command-line arguments among other things.
# Here, it checks if the command-line arguments are less than 2 (the script name and port number),
# and if so, it prints the usage message and exits.
if len(sys.argv) < 2:
    print("Usage: python server_1.py <port>")
    sys.exit(1)

# The port number is retrieved from the command-line arguments.
# sys.argv[0] is the script name, sys.argv[1] is the first argument which in this case is the port number.
port_number = int(sys.argv[1])

# The server's IP address is obtained by first getting the host name (usually the machine name)
# and then resolving it to an IP address.
server_ip = gethostbyname(gethostname())
print("*** Server is starting up on %s port %s ***" % (server_ip, port_number))

# A new socket object is created using the AF_INET address family (for IPv4) and the SOCK_STREAM type (for TCP).
sock = socket(AF_INET, SOCK_STREAM)

# The server's address is a tuple of the server IP and the port number.
server_address = (server_ip, port_number)

# The server socket is bound to the address specified earlier.
# This tells the operating system that the server is going to use this IP address and port.
sock.bind(server_address)

# The server socket is put into listening mode with a backlog of 1 connection.
# This means the server is now ready to accept connections, but it can only queue up one connection
# at a time. Additional connection attempts will get refused if there is already one in the queue.
sock.listen(1)

# A message is printed to the terminal indicating the server is ready and waiting for a connection.
print('*** Waiting for a connection ***')

# The server accepts a connection. The accept call is blocking,
# meaning that it will wait here until a client connects.
# It returns a new socket object representing the connection to the client,
# and a tuple holding the address of the client (IP and port).
connection, client_address = sock.accept()

# Once a client connects, print a message with the client's address.
print('Connection from', client_address)

try:
    # Enter a loop to receive messages from the client.
    while True:
        # Receive data from the client. The argument to recv is the buffer size.
        # It reads at most 2048 bytes from the stream at once.
        data = connection.recv(2048).decode()
        
        # If the data is an empty string or 'exit', break out of the loop,
        # which will end the connection.
        if not data or data.lower() == 'exit':
            break
        print('Client:', data)

        # Prompt the server user to input a response message.
        response = input("You: ")
        
        # Send the response message to the client.
        connection.sendall(response.encode())

# After the loop exits, close the connection to the client.
finally:
    connection.close()
    
    # Also close the server socket itself to release the port and the socket resource.
    sock.close()
    print('Server closed')
