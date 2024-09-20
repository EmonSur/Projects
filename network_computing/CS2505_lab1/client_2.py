# from the socket module import all
from socket import *

# Determine the host name and server IP
host_name = gethostname()
server_ip = gethostbyname(host_name)
print("Connecting to server at %s (%s) on port 10000" % (host_name, server_ip))

# Create a TCP socket using the "socket" method
sock = socket(AF_INET, SOCK_STREAM)

# Set values for the machine address and port number to be the same as the server is using
# but using the retrieved IP address of the machine instead of 'localhost'
server_address = (server_ip, 10000)
print('connecting to server at %s port %s' % server_address)

# Connect the socket to the host and port
sock.connect(server_address)

try:
    # Send data - now using input() to get the message from the user at runtime
    message = input("Enter the message to send to the server: ")
    print('sending "%s"' % message)
    sock.sendall(message.encode())

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        # Data is read from the connection with recv()
        data = sock.recv(64).decode()  # Adjusted buffer size to 64 for demonstration
        amount_received += len(data)
        print('received "%s"' % data)

finally:
    print('closing socket')
    sock.close()






# UCC CS2505

