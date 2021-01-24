# Sources Used: A top down approach by Kurose Ross
from socket import *
import random
import time

# Data to be returned to client
serverData= "HTTP/1.1 200 OK\r\n"\
"Content-Type: text/html; charset=UTF-8\r\n\r\n"\
"<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"

# setting up random port number
serverPort = random.randint(1023,12000)
# serverPort = 3001
print("Server Port Number", serverPort)

# creating TCP socket
serverSocket = socket(AF_INET,SOCK_STREAM)

#getfqdn gets the fully qualified domain name. Because the parameter is left blank
#this corresponds to the current local host
serverHost = getfqdn()
print("Server Host:",serverHost)

# Binding 2nd param port number and 1st param is hostname  This is the handshake socket
serverSocket.bind((serverHost, serverPort))

# Setting up maximum amount of listening sockets, this is the handshake socket
serverSocket.listen(1)

# creating client specific socket, clientAddress is the clients hostname,ip address
while True:
    connectionSocket, clientAddress = serverSocket.accept()
    print("Connected by: ", clientAddress,"\n\n")
    # Reading in client message
    read = connectionSocket.recv(2048)
    clientFile = read.decode()
    print("Received:", clientFile)
    connectionSocket.send(serverData.encode())
    print("SENDING>>>>",serverData,"\n<<<<<<<<<<<<<<")
    # Close TCP connection
    connectionSocket.close()
