# Модуль socket для сетевого программирования
from socket import *

# данные сервера
host = 'localhost'
port = 777
addr = (host, port)

# socket - функция создания сокета
# первый параметр socket_family может быть AF_INET или AF_UNIX
# второй параметр socket_type может быть SOCK_STREAM(для TCP) или SOCK_DGRAM(для UDP)
tcp_socket = socket(AF_INET, SOCK_STREAM)
# bind - связывает адрес и порт с сокетом
tcp_socket.bind(addr)
# listen - запускает прием TCP
tcp_socket.listen(1)
conn, addr = tcp_socket.accept()
print('client addr: ', addr)
# Бесконечный цикл работы программы
while True:

    # Если мы захотели выйти из программы


    print('waiting data...')

    # accept - принимает запрос и устанавливает соединение, (по умолчанию работает в блокирующем режиме)
    # устанавливает новый сокет соединения в переменную conn и адрес клиента в переменную addr


    # recv - получает сообщение TCP
    data = conn.recv(1024)
    # если ничего не прислали, завершим программу

    print(data.decode())
    # send - передает сообщение TCP
    conn.send('Message is received'.encode())
    # close - закрывает сокет

tcp_socket.close()
