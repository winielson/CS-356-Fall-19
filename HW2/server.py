# Ping Server
# Winielson Miranda, wm84, CS 356-005

import socket
import sys
import struct
import random

# Read server IP address and port from command-line arguments
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])

# Create a UDP socket. Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Assign server IP address and port number to socket
serverSocket.bind((serverIP, serverPort))

print("The server is ready to receive on port:  " + str(serverPort) + "\n")

# Loop forever listening for incoming UDP messages
while True:
    rand = random.randint(0, 10)
    # Receive and print the client data from "data" socket
    msg, address = serverSocket.recvfrom(4)
    seqnum, address = serverSocket.recvfrom(4)

    # Ping back to client
    if rand < 4:  # If the rand is < 4, server does not respond back to client
        msg = struct.pack('!I', 2)  # Packs msg as 4 byte integer in big endian; server sends 2 back
        serverSocket.sendto(msg, address)
        serverSocket.sendto(seqnum, address)
        print("Responding to ping request with sequence number " + str(int.from_bytes(seqnum, byteorder='big')))
    else:
        print("Message with sequence number " + str(int.from_bytes(seqnum, byteorder='big')) + " dropped")
