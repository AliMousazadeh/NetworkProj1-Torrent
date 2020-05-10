import socket
import sys

serverName = 'Localhost'
serverPort = 12456
bufferSize = 1024
clientSocket = socket.socket()

clientSocket.connect((serverName, serverPort))

fileName = 'rectest.txt'
path = sys.argv[4] + sys.argv[3]
clientSocket.send(path.encode())

f = open('downloaded__' + fileName, "wb")

while True:
    fileByte = clientSocket.recv(bufferSize)

    if fileByte == b'':
        break

    f.write(fileByte)

f.close()
clientSocket.close()
