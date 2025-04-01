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
    message = input("Enter the message to send to the server: ")
    print('sending "%s"' % message)
    sock.sendall(message.encode())
    
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(64).decode()
        amount_received += len(data)
        print('received "%s"' % data)
finally:
    sock.close()
    print('Socket closed.')
