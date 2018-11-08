from socket import *

host = '192.168.1.39'
port = 8081
addr = (host, port)

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind(addr)
tcp_socket.listen(1)
conn, addr = tcp_socket.accept()
print('client addr: ', addr)
while True:

    print('waiting data...')
    data = conn.recv(1024)
    print(data.decode())
    conn.send('Message is received\n'.encode())

tcp_socket.close()
