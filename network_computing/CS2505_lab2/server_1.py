from socket import *
import time
import sys

if len(sys.argv) < 2:
    print("Usage: python server_2.py <port>")
    sys.exit(1)

port_number = int(sys.argv[1])
host_name = gethostname()
server_ip = gethostbyname(host_name)
print("*** Server is starting up on %s (%s) port %s ***" % (host_name, server_ip, port_number))

sock = socket(AF_INET, SOCK_STREAM)
server_address = (server_ip, port_number)
sock.bind(server_address)
sock.listen(1)

while True:
    print('*** Waiting for a connection ***')
    connection, client_address = sock.accept()
    
    try:
        print('Connection from', client_address)
        while True:
            data = connection.recv(128).decode()
            if not data:
                break
            
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")
            client_ip, client_port = client_address
            log_message = "[%s] %s:%s\n" % (current_time, client_ip, client_port)
            print('Received "%s"' % data)
            
            with open("server_messages.log", "a") as log_file:
                log_file.write(log_message)
            acknowledgment_message = "Your message was logged at %s" % current_time
            connection.sendall(acknowledgment_message.encode())

    except ConnectionAbortedError:
        print('Connection aborted by client:', client_address)
    except Exception as e:
        print('Unexpected error:', str(e))
    finally:
        connection.close()
        print('Connection with %s closed' % (client_address,))
