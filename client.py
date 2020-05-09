import socket

serverName = 'Localhost'
serverport = 12456
bufferSize = 2048
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Traget IP: ', serverName)
print('Target Port:', serverport)
print('\n')

operator = 'Hello!'
clientSocket.sendto(operator.encode(), (serverName, serverport))
answer, serverAddress = clientSocket.recvfrom(bufferSize)
print(answer)
