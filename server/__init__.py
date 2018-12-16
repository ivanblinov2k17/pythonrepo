from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import re


def accept_incoming_connections():
    """Прием входящих соединений"""
    while True:
        client, client_address = SERVER.accept()

        client.send(bytes("Привет! Напечатайте свое имя", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # аргумент - сокет клиента
    """Логика обмена сообщениями с подключенным клиентом"""

    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Привет %s! Если вы захотите выйти, напечатайте {quit}' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s присоединился" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        try:
            msg = client.recv(BUFSIZ)
        except ConnectionResetError:
            print('Аварийный выход со стороны клиента')
            break
        if msg != bytes("{quit}", "utf8"):
            msg_string = msg.decode("utf8")
            if re.fullmatch(r"/ls\s\S*\s.*", msg_string):

                nickname = re.findall(r"/ls\s\S*", msg_string)[0][4:]

                ls_message = re.findall(r"(\S*\s)", msg_string)
                ls_message_string = ''

                for i in range(2, len(ls_message)):
                    ls_message_string += ls_message[i]
                
                print(ls_message_string)
            else:
                broadcast(msg, name + ": ")
        else:
            client.close()
            del clients[client]
            broadcast(bytes("%s покинул чат" % name, "utf8"))
            break


def broadcast(msg, prefix=""):
    """Рассылает сообщение всем клиентам"""

    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)


clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen()
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()