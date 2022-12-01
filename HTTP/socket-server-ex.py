import socket
from _thread import *

def socketThread(clientSocket, addr):

    print('addr : ', addr)

    while True:

        data = clientSocket.recv(1024)
        if not data:
            print('DISCONNECTED ADDR : ', addr)
            break

        print('RECEIVED : ', addr, data.decode())

        clientSocket.send(data)



HOST = '127.0.0.1'  #localhost
PORT = 9999

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind((HOST, PORT))
serverSocket.listen()

print('server ready~!!')


while True:
    print('wait')

    clientSocket, addr = serverSocket.accept()
    start_new_thread(socketThread, (clientSocket, addr))

serverSocket.close()
    # clientSocket.send()
    # clientSocket.recv()


