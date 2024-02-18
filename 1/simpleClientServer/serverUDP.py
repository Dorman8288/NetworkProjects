from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverPort = 100
serverSocket.bind(('', serverPort))
print("server is running!")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    result = f"Prossessd {message.decode()}"
    serverSocket.sendto(result.encode(), clientAddress)