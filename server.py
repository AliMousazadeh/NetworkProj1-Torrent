import socket

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
    print('Filename received: ', fileName)
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
