
import socket
from _thread import *
import threading
import struct
import sys


TCP_IP = '0.0.0.0'
TCP_PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(10)
write_lock = threading.Lock()


def handle_client(c, client_address):
    while True:

        # data received from client
        data = c.recv(1024)
        if not data:
            c.close()
            break
        data = data.decode('utf-8').strip()
        write_lock.acquire()
        logs = open("data.txt", "a")
        logs.write(data+"\n")
        print(data)
        logs.close()
        write_lock.release()

        respuesta = "SUCCESS"
        # Respuesta
        c.send(respuesta.encode("utf-8"))

    # connection closed


def operational():
    multicast_group = '224.3.29.71'
    server_address = ('', 10000)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind(server_address)

    group = socket.inet_aton(multicast_group)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    sock.setsockopt(
        socket.IPPROTO_IP,
        socket.IP_ADD_MEMBERSHIP,
        mreq)

    while True:
        data, address = sock.recvfrom(1024)

        sock.sendto(b'PONG-D2', address)


start_new_thread(operational, ())
while True:
    connection, client_address = s.accept()
    print('connection from', client_address)
    start_new_thread(handle_client, (connection, client_address,))
