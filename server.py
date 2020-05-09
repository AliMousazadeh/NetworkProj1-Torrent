import socket
import math
import time

serverName = 'Localhost'
serverPort = 12456
bufferSize = 2048
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('localhost', 12456))
print('Server started.')

while True:
    print('Listening...')

    operator, clientAddress = serverSocket.recvfrom(bufferSize)
    print('Operator received: ', operator)
    answer = 'Hello back!'
    serverSocket.sendto(answer.encode(), clientAddress)
    break

serverSocket.close()
