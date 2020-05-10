import socket
import sys

if (sys.argv[1] == '-receive'):
    serverName = 'Localhost'
    serverPort = 12456
    bufferSize = 1024
    clientSocket = socket.socket()

    clientSocket.connect((serverName, serverPort))

    fileName = 'rectest.txt'
    path = sys.argv[2]
    clientSocket.send(path.encode())

    f = open('downloaded__' + fileName, "wb")

    while True:
        fileByte = clientSocket.recv(bufferSize)

        if fileByte == b'':
            break

        f.write(fileByte)

    f.close()
    clientSocket.close()
elif (sys.argv[1] == '-serve'):
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

        f = open(fileName, "rb")

        fileByte = f.read(bufferSize)
        while (fileByte):
            connection.send(fileByte)
            fileByte = f.read(bufferSize)

        f.close()
        print(fileName + ' closed.')
        connection.close()
        print('Connection closed.')
        print('')
else:
    print('Invalid argument. Terminating program...')
