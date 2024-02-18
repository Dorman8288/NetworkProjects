from socket import *

serverIP = ''
serverPort = 100
clientSocket = socket(AF_INET, SOCK_DGRAM)
try:
    while True:
        message = input("Please enter Your Query:\n")
        clientSocket.sendto(message.encode(), (serverIP, serverPort))
        result, serverAddress = clientSocket.recvfrom(2048)
        print(f"your proccessed query is: {result.decode()}")
finally:
    clientSocket.close()    