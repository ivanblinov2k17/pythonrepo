from socket import *
import sys

host = 'localhost'
port = 777
addr = (host,port)

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.connect(addr)

while True:
    data = input('write to server: ')
    if data == 'quit':
        data = str.encode(data)
        tcp_socket.send(data)
        tcp_socket.close()
        sys.exit(1)

    data = str.encode(data)
    tcp_socket.send(data)
    data = tcp_socket.recv(1024)
    print(data.decode())



