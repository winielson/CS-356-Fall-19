# Echo Client
# Winielson Miranda, wm84, CS 356-005

import sys
import socket

# Get the server hostname, port and data length as command line arguments
host = sys.argv[1]
port = int(sys.argv[2])
count = int(sys.argv[3])
data = 'X' * count  # Initialize data to be sent

it = 0  # Loop iterator

# Create UDP client socket. Note the use of SOCK_DGRAM
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsocket.settimeout(1)  # Sets timeout for 1 second

while it < 3:
    try:
        # Send data to server
        print("Sending data to " + host + ", " + str(port) + ": " + data)
        clientsocket.sendto(data.encode(), (host, port))

        # Receive the server response
        dataEcho, address = clientsocket.recvfrom(count)
        if len(address) is not None:
            print("Receive data from " + address[0] + ", " + str(address[1]) + ": " + dataEcho.decode())
            exit()
    except socket.timeout:
        print('Message timed out')
        it += 1
        if it >= 3:
            exit()



#Close the client socket
clientsocket.close()
