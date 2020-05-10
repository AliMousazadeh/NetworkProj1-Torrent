import socket
import sys

serverName = 'Localhost'
serverPort = 12456
bufferSize = 1024
clientSocket = socket.socket()

clientSocket.connect((serverName, serverPort))

fileName = sys.argv[2]
clientSocket.send(fileName.encode())

f = open('downloaded__' + fileName, "wb")

while True:
    fileByte = clientSocket.recv(bufferSize)

    if fileByte == b'':
        break

    f.write(fileByte)

f.close()
clientSocket.close()
