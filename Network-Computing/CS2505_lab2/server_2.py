# from the socket module import all
from socket import *
import sys

if len(sys.argv) < 2:
    print("Usage: python server_1.py <port>")
    sys.exit(1)

port_number = int(sys.argv[1])
server_ip = gethostbyname(gethostname())
print("*** Server is starting up on %s port %s ***" % (server_ip, port_number))

sock = socket(AF_INET, SOCK_STREAM)
server_address = (server_ip, port_number)
sock.bind(server_address)
sock.listen(1)

print('*** Waiting for a connection ***')
connection, client_address = sock.accept()

print('Connection from', client_address)

try:
    while True:
        # Receive data
        data = connection.recv(2048).decode()
        if not data or data.lower() == 'exit':
            break
        print('Client:', data)

        # Send response
        response = input("You: ")
        connection.sendall(response.encode())

finally:
    connection.close()
    sock.close()
    print('Server closed')

