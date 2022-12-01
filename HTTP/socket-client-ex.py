import socket
#'192.168.0.49'

HOST = '127.0.0.1'
# HOST = '192.168.0.49'
PORT = 9999

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((HOST, PORT))

while True:
    
    inputText = input('Send messages: ')
    clientSocket.send(inputText.encode())

    data = clientSocket.recv(1024)
    print('RECEIVED MESSAGES : ', data.decode())