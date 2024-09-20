# Import the socket module to use the necessary network functionalities.
from socket import *
# Import the sys module to access command-line arguments.
import sys

# Check if the correct number of command-line arguments has been provided,
# otherwise, print usage instruction and exit the script.
if len(sys.argv) < 2:
    print("Usage: python server_2.py <port>")
    sys.exit(1)

# Convert the second command-line argument to an integer to use as the port number.
port_number = int(sys.argv[1])
# Retrieve the host name of the machine the script is running on.
host_name = gethostname()
# Retrieve the IP address associated with the host name.
server_ip = gethostbyname(host_name)
# Print the IP and port information where the server will start.
print("*** Server is starting up on %s (%s) port %s ***" % (host_name, server_ip, port_number))

# Create a TCP/IP socket.
sock = socket(AF_INET, SOCK_STREAM)
# Prepare the server address using the retrieved IP and the given port number.
server_address = (server_ip, port_number)
# Bind the socket to the server address.
sock.bind(server_address)
# Listen for incoming connections with a queue of 1 connection.
sock.listen(1)

# Start an infinite loop to keep the server running.
while True:
    # Inform that the server is waiting for a connection.
    print('*** Waiting for a connection ***')
    # Accept a connection when a client attempts to connect, and retrieve the connection object and the client address.
    connection, client_address = sock.accept()
    
    try:
        # Print the client's address information upon establishing a connection.
        print('Connection from', client_address)
        # Continue receiving data from the client until the connection is closed.
        while True:
            # Receive data from the client, with a buffer size of 128 bytes, and decode it to a string.
            data = connection.recv(128).decode()
            # If no data is received, this implies the client has closed the connection, so break out of the loop.
            if not data:
                break
            # Retrieve the current time and format it in Year-Month-Day Hour:Minute:Second.
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")
            # Print the received message to the console.
            print('Received "%s"' % data)
            # Log the client's IP, port, and the current time to a log file named 'server_messages.log'.
            with open("server_messages.log", "a") as log_file:
                log_file.write("[%s] %s:%s\n" % (current_time, client_address[0], client_address[1]))
            # Prepare an acknowledgment message containing the time the message was logged.
            acknowledgment_message = "Your message was logged at %s" % current_time
            # Send the acknowledgment message back to the client.
            connection.sendall(acknowledgment_message.encode())

    # Handle the specific exception where the connection is aborted by the client.
    except ConnectionAbortedError:
        print('Connection aborted by client:', client_address)
    # Handle any other unexpected exceptions.
    except Exception as e:
        print('Unexpected error:', str(e))
    # The 'finally' block is executed after try block finishes execution, whether an exception occurred or not.
    finally:
        # Close the client connection once the while loop is exited.
        connection.close()
        # Print a message indicating that the connection with the client has been closed.
        print('Connection with %s closed' % (client_address,))

# Close the server socket when the server stops running.
sock.close()
