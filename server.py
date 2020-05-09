import socket

serverName = 'Localhost'
serverPort = 12456
bufferSize = 2048
maxClients = 10
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('localhost', 12456))
print('Server started.')

serverSocket.listen(maxClients)

while True:
    c, addr = serverSocket.accept()
    print('Connection stablished with: ', addr)
    c.send('Thank you.')
    c.close
