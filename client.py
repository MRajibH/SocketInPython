# import socket module
import socket
# Create a client socket using the python socket module
clientSocket = socket.socket()
# connect with previously created server on specific port number
clientSocket.connect(('localhost',9991))

# Prompting client for his/her name
name = input("Enter your name: ")
# Send name of client to server 
clientSocket.send(bytes(name,'utf-8'))
# reciving message from server
print(clientSocket.recv(1024).decode())