# Ping Client
# Winielson Miranda, wm84, CS 356-005

import socket
import sys
import time
import struct

# Get the server hostname, port and data length as command line arguments
host = sys.argv[1]
port = int(sys.argv[2])

psent = 0
preceived = 0
plost = 0.0
rttlist = []

print("Pinging " + host + ", " + str(port))
for seqnum in range(1, 11):  #
    # Create UDP client socket. Note the use of SOCK_DGRAM
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSocket.settimeout(1)  # Sets timeout for 1 second
    msg = 1
    start = time.time()  # Initialize starting time

    # Send data to server
    # Packs msg and seqnum as 4 byte integers in big endian; client sends msg 1 to server
    clientSocket.sendto(struct.pack('!I', 1), (host, port))
    clientSocket.sendto(struct.pack('!I', seqnum), (host, port))
    psent += 1

    # Receive the server response
    try:
        rcvmsg, address = clientSocket.recvfrom(4)
        rcvseqnum, address = clientSocket.recvfrom(4)
        end = time.time()  # Timer stops when packet received
        rtt = end - start  # Round trip time is calculated
        rttlist.append(rtt)
        print("Ping message number " + str(int.from_bytes(rcvseqnum, byteorder='big')) + " RTT: " + str(rtt))
        # print("Ping message number " + str(seqnum) + " RTT: " + str(rtt))
        # print("Ping rcvmsg " + str(str(int.from_bytes(rcvmsg, byteorder='big'))))

        preceived += 1
    except socket.timeout:
        # print("Ping message number " + str(int.from_bytes(seqnum, byteorder='big')) + " timed out")
        print("Ping message number " + str(seqnum) + " timed out")
        plost += 1

plostrate = plost / psent * 100
print("\nNumber of packets sent: " + str(psent))
print("Number of packets received: " + str(preceived))
print("Percent of packets lost: " + str(plostrate) + " %")

minrtt = min(rttlist)
maxrtt = max(rttlist)
avgrtt = sum(rttlist) / len(rttlist)
print("\nFastest RTT: " + str(minrtt))
print("Slowest RTT: " + str(maxrtt))
print("Average RTT: " + str(avgrtt))

# Close the client socket
clientSocket.close()
