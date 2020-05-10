import socket
import sys

serverName = 'Localhost'
serverPort = 12456
bufferSize = 1024
maxConnections = 5
serverSocket = socket.socket()
serverSocket.bind(('localhost', serverPort))
print('Server started.')

serverSocket.listen(maxConnections)
while True:
    print('Listening...')
    connection, addr = serverSocket.accept()
    print('Connection accepted.')

    fileName = connection.recv(bufferSize)
    fileName = str(fileName.decode())
    filePath = sys.argv[5]
    print('Filename received: ', fileName)

    if (fileName != sys.argv[3]):
        print('Mismatched names. Terminating program...')
        break

    f = open(filePath, "rb")

    fileByte = f.read(bufferSize)
    while (fileByte):
        connection.send(fileByte)
        fileByte = f.read(bufferSize)

    f.close()
    print(fileName + ' closed.')
    connection.close()
    print('Connection closed.')
    print('')
