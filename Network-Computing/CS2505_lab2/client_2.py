# from the socket module import all
from socket import *
import sys

if len(sys.argv) < 3:
    print("Usage: python client_2.py <server_ip> <port>")
    sys.exit(1)

server_ip = sys.argv[1]
port_number = int(sys.argv[2])
print("Connecting to server at %s on port %s" % (server_ip, port_number))

sock = socket(AF_INET, SOCK_STREAM)
server_address = (server_ip, port_number)
sock.connect(server_address)

try:
    while True:
        message = input("You: ")
        if message.lower() == 'exit':
            break

        # Send data
        sock.sendall(message.encode())

        # Wait for response
        data = sock.recv(2048).decode()
        print('Server:', data)

finally:
    print('Closing socket')
    sock.close()
