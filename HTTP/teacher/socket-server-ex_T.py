
import socket
from _thread import *

def socketThread(clinenSocket, addr):

    print('addr:', addr)
    while True:
        
        data = clinenSocket.recv(1024)
        if not data:
            print('Disconnected addr:', addr)
            break

        print('Received addr: ',addr, data.decode())

        clientSocket.send(data)


# HOST = '127.0.0.1'  #localhost
HOST = '192.168.0.49'  #localhost
PORT = 9999

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind((HOST, PORT))
serverSocket.listen()

print('server start')

while True:
    print('wait')

    clientSocket, addr = serverSocket.accept()
    start_new_thread(socketThread, (clientSocket, addr))

serverSocket.close()