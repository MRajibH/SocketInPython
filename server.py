# Importing socket module of python
from os import name
import socket

# Creating a socket for server using soket module
serverSocket = socket.socket()
print("Socket created")

# Binding socket with a port number
serverSocket.bind(('localhost',9991))
# listenting for client to make a request
serverSocket.listen(1)
print('Waiting for connections')

# listen continiously
while True:
    # Reciving client soket name and address
    clientSocket, address = serverSocket.accept()
    name = clientSocket.recv(1024).decode()
    # printing the address of client
    print(f"connected with {name} {address}")

    clientSocket.send(bytes(" Hello from server" , 'utf-8'))
    clientSocket.close()
