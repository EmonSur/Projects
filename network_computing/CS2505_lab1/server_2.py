# from the socket module import all
from socket import *
import time

host_name = gethostname()
server_ip = gethostbyname(host_name)
print("*** Server is starting up on %s (%s) port 10000 ***" % (host_name, server_ip))

# Create a TCP server socket
sock = socket(AF_INET, SOCK_STREAM)

server_address = (server_ip, 10000)
print('*** Server is binding to %s port %s ***' % server_address)

sock.bind(server_address)

# Listen for one incoming connection to the server
sock.listen(1)

# Set up a forever true while loop for the server to run all the time
while True:
    print('*** Waiting for a connection ***')
    connection, client_address = sock.accept()
    
    try:
        print('Connection from', client_address)

        while True:
            try:
                data = connection.recv(128).decode()
                if not data:
                    print('No more data from', client_address)
                    break
                
                current_time = time.strftime("%Y-%m-%d %H:%M:%S")
                print('Received "%s"' % data)

                # Log and acknowledge in one send to prevent potential issues with client disconnects
                log_message = "[%s] %s: %s" % (current_time, client_address, data)
                with open("server_messages.log", "a") as log_file:
                    log_file.write(log_message + "\n")
                acknowledgment_message = "Your message was logged at %s" % current_time
                connection.sendall(acknowledgment_message.encode())
                print('Sending acknowledgment back to the client')

            except ConnectionAbortedError:
                print('Connection aborted by client:', client_address)
                break
            except Exception as e:
                print('Unexpected error:', str(e))
                break

    finally:
        connection.close()
        print('Connection with %s closed' % (client_address,))



# now close the socket
sock.close()



# UCC CS2505
