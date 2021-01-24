# Sources Used: A top down approach by Kurose Ross
from socket import *

# Get Request For File
getRequest= "GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"

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

# recieving data from server, 1st param is the number of bytes to recieve
serverFile = clientSocket.recv(2048)

print(serverFile.decode())
# Telling Server to close TCP connectioon
clientSocket.close()
