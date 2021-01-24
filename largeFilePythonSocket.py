# Sources Used: A top down approach by Kurose Ross
from socket import *

# Get Request For File
getRequest= "GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"

# Remote Host with cannonical name and port number
remoteHost = 'gaia.cs.umass.edu'
remotePort = 80

# creating client socket. 1st param is the address type, 2nd param is defining the socket as TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# Initial Handshake with remote server to establish new port for client
clientSocket.connect((remoteHost, remotePort))

# encode - changes from string type to byte type
# sending http file request
clientSocket.send(getRequest.encode())

# This is to initially read the first 2048 bytes into the read variable which is then shoved into the serverFile variable
# recieving data from server, 1st param is the number of bytes to recieve
read = clientSocket.recv(2048)
serverFile = read.decode()

#Continously read from the socket until read doesn't pick anything up. Store and convert the server bytes into the server
# file variable
while read != b"":
    # Doesnt seem to matter but the b in front of the "" makes it a empty byte string. But works without 
    read =  b""
    read = clientSocket.recv(2048)
    serverFile = serverFile + read.decode()

print(serverFile)

# Telling Server to close TCP connectioon
clientSocket.close()
