import socket
import sys

serverName = 'Localhost'
serverPort = 12456
bufferSize = 1024
clientSocket = socket.socket()

print('Traget IP: ', serverName)
print('Target Port:', serverPort)
print('')

clientSocket.connect((serverName, serverPort))

fileName = 'rectest.txt'
clientSocket.send(fileName.encode())

f = open('downloaded__' + fileName, "wb")

while True:
    fileByte = clientSocket.recv(bufferSize)

    if fileByte == b'':
        break

    f.write(fileByte)

f.close()
clientSocket.close()
